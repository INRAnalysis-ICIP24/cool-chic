import torch

class L1Loss(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def __call__(self, img1, img2):
        diff = img1 - img2
        return torch.mean(torch.abs(diff))

