from typing import Dict

"""CNN model architecture"""

def build_cnn(layers) -> Dict:
    """
        Build a CNN model
    """
    print(f"==Building CNN with {layers} layers==")
    return {"model_type": "cnn", "layers": layers}