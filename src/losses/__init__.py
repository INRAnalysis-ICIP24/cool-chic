import sys
from losses.composite import CompositeLoss

from losses.l1 import L1Loss
from losses.l2 import L2Loss
from losses.log_cosh import LogCoshLoss
from losses.ssim import DSSIMLoss

def loss_from_id(id):
    if id == "l1":
        return L1Loss()
    if id == "mse":
        return L2Loss()
    if id == "log_cosh":
        return LogCoshLoss()
    if id == "ssim":
        return DSSIMLoss()

def build_loss(config):
    components_configs = config.split()
    components = list()
    for component_config in components_configs:
        identifier, weight = component_config.split(":")
        weight = float(weight)

        component = loss_from_id(identifier)
        components.append((component, weight))
            
    return CompositeLoss(components)
