from typing import Dict

"""Model training utilities"""

def train_model(model, data, epochs) -> Dict:
    """
        Train the model
    """
    print(f"==Training model==")
    print(f"Epochs : {epochs}")
    for epoch in range(epochs):
        print(f"  Epoch {epoch + 1}/{epochs}")
    return {"trained": True, "epochs": epochs}

def evaluate_model(model, test_data) -> Dict:
    """
        Evaluate model performance
    """
    print("==Evaluating model==")
    return {"accuracy": 0.95, "loss": 0.05}