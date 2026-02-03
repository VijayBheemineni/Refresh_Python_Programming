from typing import Dict

"""Optimizer configurations"""

def configure_optimizer(optimizer_type, learning_rate) -> Dict:
    """
        Configure optimizer
    """
    print(f"==Configuring optimizer==")
    return {"optimizer": optimizer_type, "lr": learning_rate}
