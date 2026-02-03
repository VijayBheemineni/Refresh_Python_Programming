"""Data loader module"""
from typing import Dict

def load_data(source : str) -> Dict:
    """
        Load data from source

        Args:
            source: Source from where data is loaded.
        Returns:
            Dictionary which contains 'status' and'source'
        Raises:
            None
    """
    print(f"**Loading data from {source}**")
    return {"status" : "success", "source": source}

def load_batch(batch_size : int) -> Dict:
    """
        Load data in batches

        Args:
            batch_size: batch size
        Returns:
            Dictionary which contains 'batch_size' and'samples'
        Raises:
            None
    """
    print(f"Loading batch of size {batch_size}...")
    return {"batch_size": batch_size, "samples": []}