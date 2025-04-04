"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ITagungPloneDeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


# XXX: deprecated, do not use this interface!!!
class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
