"""Subpackage for deployment"""

print("Hello from deployment subpackage!")

from aimodel.deployment.exporter import export_model
from aimodel.deployment.api import create_api

__all__ = ['export_model', 'create_api']