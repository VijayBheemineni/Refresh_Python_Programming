"""
    Example usage of aimodel package
"""

# Import entire package
import aimodel

# Import specific subpackages
from aimodel.data import loader, preprocessor
from aimodel.models import transformer, cnn 
from aimodel.training import trainer, optimizer
from aimodel.deployment import exporter, api

# Use the package
print("\n=== Data Processing ===")
data = loader.load_data("dataset.csv")
processed_data = preprocessor.preprocess(data)

print("\n=== Model Building ===")
model = transformer.build_transformer({"layers": 6, "heads": 8})

print("\n=== Training ===")
opt = optimizer.configure_optimizer("adam", 0.001)
trained_model = trainer.train_model(model, processed_data, epochs=10)

print("\n=== Deployment ===")
exporter.export_model(trained_model, format="onnx")
api.create_api(trained_model, port=8000)

print("SUCCESS")