from . import logger


from .base import reload_gs_profile

# from plone import api


def upgrade(setup_tool=None):
    """ """
    logger.info(
        "Running upgrade (Python): load control panel setting"
        " to allow setting Time Box Types"
    )
    reload_gs_profile(setup_tool)
