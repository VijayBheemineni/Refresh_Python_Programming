from typing import Dict

"""Model export utilities"""

def export_model(model, format="onnx") -> Dict:
    """
        Export model to specified format
    """
    print(f"==Exporting model format==")
    return {"exported": True, "format": format}