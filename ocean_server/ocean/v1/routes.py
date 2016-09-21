"""
index.py module for ocean
"""

# Standard library imports
import logging

# Third party imports
from kyoukai.context import HTTPRequestContext

# Local imports
from .blueprint import blueprint


log = logging.getLogger(__name__)


@blueprint.add_route('/', methods=['GET'])
async def index(ctx: HTTPRequestContext):
    """Index route"""
    return "hello world"
