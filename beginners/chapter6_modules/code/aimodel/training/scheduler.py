from typing import Dict
"""Learning rate schedulers"""

def create_scheduler(schedule_type) -> Dict:
    """
        Create learning rate scheduler
    """
    print(f"==Creating scheduler==")
    return {"scheduler": schedule_type}