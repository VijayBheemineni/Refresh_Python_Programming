from typing import Dict

"""API deployment utilities"""

def create_api(model, port=8000) -> Dict:
    """
        Create REST API for model
    """
    print(f"==Creating API==")
    return {"api_running": True, "port": port}

def serve_model(model, endpoint) -> Dict:
    """
        Serve model at endpoint
    """
    print(f"==Serving model==")
    return {"serving": True, "endpoint": endpoint}