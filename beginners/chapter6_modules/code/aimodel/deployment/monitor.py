from typing import Dict

"""Model monitoring utilities"""

def monitor_performance(model) -> Dict:
    """
        Monitor model performance in production
    """
    print("==Monitoring model performance==")
    return {"monitoring": True, "metrics": {}}

def log_predictions(predictions) -> Dict:
    """
        Log model predictions
    """
    print(f"==Logging predictions==")
    return {"logged": True}