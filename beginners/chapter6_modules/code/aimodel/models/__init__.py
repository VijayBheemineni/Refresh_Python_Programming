"""Subpackage for model architectures"""
print("Hello from models subpackage!")

from aimodel.models.transformer import build_transformer
from aimodel.models.cnn import build_cnn

__all__ = ['build_transformer', 'build_cnn']

