"""
container.py module for ocean
"""

# Standard library imports
import logging

# Third party imports
from asphalt.core import ContainerComponent, Context
from kyoukai import KyoukaiComponent

# Local imports
from .ocean import get_ocean


log = logging.getLogger(__name__)


class OceanContainer(ContainerComponent):
    """A container for the app"""
    async def start(self, ctx: Context):
        ocean = get_ocean()
        self.add_component(
            'web', KyoukaiComponent, ip='127.0.0.1', port=4444, app=ocean
        )
        await super().start(ctx)
