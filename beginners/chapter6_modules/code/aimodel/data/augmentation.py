from typing import Dict


"""Data augmentation module"""

def augment_data(data) -> Dict:
    """
        Augment training data
    """
    print("==Augmenting data for better training==")
    return {"augmented": True, "original": data}