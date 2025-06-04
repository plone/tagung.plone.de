from tagung.plone.de.content.time_box import ITimeBoxBase
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """Dummy to prevent indexing other objects thru acquisition"""
    raise AttributeError("This field should not indexed here!")


@indexer(ITimeBoxBase)  # ADJUST THIS!
def talk_timetable(obj):
    """Calculate and return the value for the indexer"""
    info = ""
    info += str(int(obj.start.timestamp()))
    if hasattr(obj, "room"):
        info += obj.room
    return info
