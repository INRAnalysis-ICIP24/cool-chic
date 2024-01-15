import torch

class CompositeLoss:
    def __init__(self, losses, return_components=False):
        self.__losses = losses
        self.__return_components = return_components
    
    def __len__(self):
        return len(self.__losses)

    def __call__(self, *args):
        losses = list()
        components = dict()
        for (loss_fn, delta) in self.__losses:
            loss = loss_fn(*args)
            losses.append((loss * delta).reshape(1))
            components[type(loss_fn).__name__] = loss

        total_loss = torch.cat(losses).mean()

        if self.__return_components:
            return total_loss, components
        else:
            return total_loss

    def __repr__(self) -> str:
        return f"CompositeLoss({self.__losses})"

