from . import logger
from .base import reload_gs_profile

# from plone import api


def upgrade(setup_tool=None):
    """ """
    logger.info(
        "Running upgrade (Python): load catalog settings to enable "
        "type_of_time_box meta column"
    )
    reload_gs_profile(setup_tool)
