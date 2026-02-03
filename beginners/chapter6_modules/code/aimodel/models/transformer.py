from typing import Dict

"""Transformer model architecture"""

def build_transformer(config) -> Dict :
    """
        Build a transformer model
    """
    print("==Building transformer model==")
    print(f"Config: {config}")
    return {"model_type": "transformer", "config": config}

