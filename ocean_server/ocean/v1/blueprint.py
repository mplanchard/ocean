"""
blueprint.py module for ocean
"""

# Standard library imports
import logging

# Third party imports
from kyoukai import Blueprint

# Local imports


log = logging.getLogger(__name__)


blueprint = Blueprint('ocean_v1', url_prefix='v1')
