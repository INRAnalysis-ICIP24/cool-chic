import math
import torch

def log_cosh(x: torch.Tensor) -> torch.Tensor:
    return x + torch.nn.functional.softplus(-2. * x) - math.log(2.0)

class LogCoshLoss(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(
        self, y_pred: torch.Tensor, y_true: torch.Tensor
    ) -> torch.Tensor:
        diff = y_pred - y_true
        return torch.mean(log_cosh(diff))
