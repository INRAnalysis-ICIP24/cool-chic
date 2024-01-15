# Software Name: Cool-Chic
# SPDX-FileCopyrightText: Copyright (c) 2023 Orange
# SPDX-License-Identifier: BSD 3-Clause "New"
#
# This software is distributed under the BSD-3-Clause license.
#
# Authors: Theo Ladune <theo.ladune@orange.com>
#          Pierrick Philippe <pierrick.philippe@orange.com>

from losses import build_loss
import torch
import sys

from typing import Dict, Tuple, Union
from torch import Tensor
from model_management.yuv import DictTensorYUV
from utils.ms_ssim import MSSSIM


def mse_fn(x: Tensor, y: Tensor) -> Tensor:
    """Compute the Mean Squared Error of two tensors with arbitrary dimension.

    Args:
        x and y (Tensor): Compute the MSE of x and y.

    Returns:
        Tensor: One element tensor containing the MSE of x and y.
    """
    return torch.pow((x - y), 2.0).mean()


def loss_fn(
    out_forward: Dict[str, Tensor],
    target: Union[Tensor, DictTensorYUV],
    lmbda: float,
    compute_logs: bool = False,
    dist_mode: str = 'mse:1.0',
    rate_mlp: float = 0.,
) -> Tuple[Tensor, Dict]:
    """Compute the loss and other quantities from the network output out_forward

    Args:
        out_forward (dict): Contains x_hat [1, 3, H, W], a tensor with the decoded
            image and rate_y a one-element tensor containing the total rate in bits
            for the y latent variable
        target (Union[Tensor, DictTensorYUV]):
            Either a [1, 3, H, W] tensor of the ground truth image (RGB444) or a
            dictionary with 3 4d tensors for Y, U & V.
        lmbda (float): Rate constraint
        compute_logs (bool, Optional): If true compute additional quantities. This
            includes the MS-SSIM Which in turn requires that out_forward describes the
            entire image. Default to False.
        dist_mode (bool, Optional): Either 'mse' or 'ms_ssim'. If ms_ssim we need
            out_forward and target to be the entire image i.e. of shape [H * W, 3].
            Default to mse.
        rate_mlp (float, Optional): Rate of the network if it needs to be present in the
            loss computation. Expressed in bit! Default to 0.

    Returns:
        Tuple: return loss and log dictionary (only if compute_logs)
    """

    x_hat = out_forward.get('x_hat')

    flag_yuv = not(isinstance(target, Tensor))
    if flag_yuv:
        print(f"YUV is not supported in this fork")
        sys.exit(1)

    n_pixels = x_hat.size()[-2] * x_hat.size()[-1]

    rate_bpp = (out_forward.get('rate_y').sum() + rate_mlp) / n_pixels

    dist_fn = build_loss(dist_mode)
    dist = dist_fn(x_hat, target)
    # dist = mse
    loss = dist + lmbda * rate_bpp

    if compute_logs:
        logs = {
            'loss': loss.detach().item(),
            'dist': dist.detach().item(),
            'rate_mlp': rate_mlp / n_pixels,        # Rate MLP in bpp
            'rate_y': out_forward.get('rate_y').detach().sum().item() / n_pixels,  # Rate y in bpp
        }

        # Append the different rates (in bpp) to the log
        # for k, v in out_forward.items():
            # if 'rate' not in k:
                # continue
            # # Ignore lists which are due to the comprehensive rate_per_grid tensor
            # if isinstance(v, list):
                # continue
            # if isinstance(v, Tensor):
                # v = v.detach().item()
            # logs[k] = v / n_pixels

        logs['rate_all_bpp'] = logs.get('rate_mlp') + logs.get('rate_y')

        logs['rate_per_latent_bpp'] = [
            rate_cur_ft.sum() / n_pixels for rate_cur_ft in out_forward.get('2d_y_rate')
        ]

    else:
        logs = None

    return loss, logs
