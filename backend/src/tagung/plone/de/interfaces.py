"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ITagungPloneDeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
