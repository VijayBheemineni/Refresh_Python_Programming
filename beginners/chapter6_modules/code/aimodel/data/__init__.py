"""Subpackage for data processing"""

print("Hello from data subpackage!")

from aimodel.data.loader import load_data
from aimodel.data.preprocessor import preprocess

__all__ = ['load_data', 'preprocess']
