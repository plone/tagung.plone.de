from plone.app.event.base import default_timezone
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import Invalid, implementer, invariant
from zope.interface import Interface

from tagung.plone.de import _


class StartBeforeEnd(Invalid):
    __doc__ = _("error_invalid_date", default="Invalid start or end date")


class ITimeBoxBase(Interface):
    """Marker for Time Box and Talk"""


class ITimeBox(model.Schema, ITimeBoxBase):
    """Marker interface and Dexterity Python Schema for TimeBox"""

    type_of_time_box = schema.Choice(
        title=_(
            "Time Box Type",
        ),
        # description=_(
        #     u'',
        # ),
        vocabulary="tagung.time_box.type_of_time_box",
        default=None,
        # defaultFactory=get_default_timebox_type,
        required=False,
        readonly=False,
    )

    directives.write_permission(room="cmf.ReviewPortalContent")
    room = schema.Choice(
        title=_("Room"),
        vocabulary="tagung.talk.room",
        required=False,
    )

    directives.widget(
        "start",
        default_timezone=default_timezone,
        klass="event_start",
    )
    directives.write_permission(start="cmf.ReviewPortalContent")
    start = schema.Datetime(
        title=_(
            "Start",
        ),
        # defaultFactory=get_default_start,
        required=True,
        readonly=False,
    )

    directives.widget(
        "end",
        default_timezone=default_timezone,
        klass="event_end",
        pattern_options={
            "behavior": "styled",
            "after": "input.event_end",
            "offset-days": "0.125",
        },
    )
    directives.write_permission(end="cmf.ReviewPortalContent")
    end = schema.Datetime(
        title=_(
            "End",
        ),
        # defaultFactory=get_default_start,
        required=True,
        readonly=False,
    )

    @invariant
    def validate_start_end(data):
        if data.start and data.end and data.start > data.end and not data.open_end:
            raise StartBeforeEnd(
                _(
                    "error_end_must_be_after_start_date",
                    default="End date must be after start date.",
                )
            )


@implementer(ITimeBox)
class TimeBox(Item):
    """Content-type class for ITimeBox"""
