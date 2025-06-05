from . import logger


from .base import reload_gs_profile

# from plone import api


def upgrade(setup_tool=None):
    """ """
    logger.info(
        "Running upgrade (Python): load registry to update type_of_talk query string"
    )
    reload_gs_profile(setup_tool)
