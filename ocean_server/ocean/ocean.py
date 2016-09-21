"""
ocean.py module for ocean
"""

# Standard library imports
import logging

# Third party imports
from kyoukai import Kyoukai

# Local imports
from .v1.blueprint import blueprint


log = logging.getLogger(__name__)


def get_ocean():
    """Get the ocean application object"""
    ocean = Kyoukai('ocean')
    ocean.register_blueprint(blueprint)
    return ocean
