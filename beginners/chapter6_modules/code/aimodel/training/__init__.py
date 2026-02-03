"""Subpackage for training utilities"""

print("Hello from training subpackage!")

from aimodel.training.trainer import train_model
from aimodel.training.optimizer import configure_optimizer

__all__ = ['train_model', 'configure_optimizer']
