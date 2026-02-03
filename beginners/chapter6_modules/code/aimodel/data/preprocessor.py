from typing import Dict, List

"""Data preprocessor module"""

def preprocess(data) -> Dict:
    """
        Preprocess the data
    """
    print("==Preprocessing Data==")
    return {"preprocessed": True, "data": data}


def normalize(data) -> Dict:
    """
        Normalize data
    """
    print("==Normalizing Data==")
    return data


def tokenize(text) -> List:
    """
        Tokenize text data
    """
    print(f"===Tokenizing text===")
    print(f"text : {text}")
    return text.split()