from typing import Dict


"""RNN model architecture"""

def build_rnn(units) -> Dict:
    """
        Build an RNN model
    """
    print(f"==Building RNN with {units} units==")
    return {"model_type": "rnn", "units": units}

