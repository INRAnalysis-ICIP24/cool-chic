import torch

class L2Loss(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def __call__(self, original, prediction):
        diff = original - prediction
        return diff.square().mean()
