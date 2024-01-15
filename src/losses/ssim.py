import torch
from pytorch_msssim import ssim

class DSSIMLoss:
    def __init__(self):
        pass

    def __call__(self, original, distorted):
        ssim_val = ssim(
            original, 
            distorted, 
            data_range=1.0
        )

        return (1.0 - ssim_val)
