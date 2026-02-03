"""
AI Model Package - Hello World Example
A package for building, training, and deploying AI models for my understanding
"""
print("Hello from aimodel package!")

__version__ = "0.1.0"
__author__ = "Vijay Bheemineni"

from aimodel.models import transformer, cnn

__all__ = ['transformer', 'cnn']