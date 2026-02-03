from typing import Dict

"""Custom model architectures"""

def build_custom(architecture):
    """
        Build a custom model
    """
    print(f"Hello! Building custom model: {architecture}...")
    return {"model_type": "custom", "architecture": architecture}