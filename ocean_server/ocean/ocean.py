"""
ocean.py module for ocean
"""

# Standard library imports
import json
import logging

# Third party imports
from kyoukai import Kyoukai
from kyoukai.context import HTTPRequestContext
import kyoukai.exc as ke

# Local imports
from .v1.routes import blueprint
from .v1 import routes


log = logging.getLogger(__name__)


def get_ocean():
    """Get the ocean application object"""
    ocean = Kyoukai('ocean')
    ocean.debug = True
    ocean.register_blueprint(blueprint)

    top_level_route = '(?!{}).*'.format(blueprint.prefix)

    @ocean.route(top_level_route, methods=['GET'])
    async def index(ctx: HTTPRequestContext):
        app = ctx.app
        route = blueprint.prefix + ctx.request.path
        v1_route = app.root.match(route, method=ctx.request.method)
        if v1_route is not None:
            # return 'would call %s' % v1_route
            return await v1_route.invoke(ctx)
        else:
            raise ke.HTTPException(404)

    return ocean
