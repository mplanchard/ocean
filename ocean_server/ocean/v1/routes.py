"""
index.py module for ocean
"""

# Standard library imports
import logging

# Third party imports
from kyoukai import Blueprint
from kyoukai.context import HTTPRequestContext

# Local imports
# from .blueprint import blueprint


log = logging.getLogger(__name__)

blueprint = Blueprint('ocean_v1', url_prefix='/v1')


@blueprint.route('/', methods=['GET'])
async def v1_index(ctx: HTTPRequestContext):
    """Index route"""
    return 'hello world'


@blueprint.route('/test', methods=['GET'])
async def test(ctx: HTTPRequestContext):
    """Index route"""
    return "hello world test!"
