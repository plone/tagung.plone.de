from plone.app.event.base import default_timezone
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from tagung.plone.de import _
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import Invalid
from zope.interface import invariant


class StartBeforeEnd(Invalid):
    __doc__ = _("error_invalid_date", default="Invalid start or end date")


class ITalk(model.Schema):
    """Talk content type schema"""

    directives.widget(type_of_talk=RadioFieldWidget)
    type_of_talk = schema.Choice(
        title=_("Type of talk"),
        vocabulary="tagung.talk.type_of_talk",
        required=True,
        # max_length=3000,
    )

    details = RichText(
        title=_("Details"),
        description=_(
            "Description of the talk (max. 3000 characters). To format select some text."
        ),
        max_length=3000,
        required=True,
    )

    directives.widget(audience=CheckBoxFieldWidget)
    directives.write_permission(audience="cmf.ReviewPortalContent")
    audience = schema.Set(
        title=_("Audience"),
        value_type=schema.Choice(
            vocabulary="tagung.talk.audience",
        ),
        required=False,
    )

    directives.write_permission(room="cmf.ReviewPortalContent")
    room = schema.Choice(
        title=_("Room"),
        vocabulary="tagung.talk.room",
        required=False,
    )

    speaker = schema.TextLine(
        title=_("Speaker"),
        description=_("Name (or names) of the speaker"),
        required=False,
    )

    company = schema.TextLine(
        title=_("Company"),
        required=False,
    )

    email = Email(
        title=_("Email"),
        description=_("Email address of the speaker"),
        required=False,
    )

    website = schema.TextLine(
        title=_("Website"),
        required=False,
    )

    mastodon = schema.TextLine(
        title=_("Mastodon URL"),
        required=False,
    )

    github = schema.TextLine(
        title=_("Github username"),
        required=False,
    )

    image = NamedBlobImage(
        title=_("Image"),
        description=_("Portrait of the speaker"),
        required=False,
    )

    speaker_biography = RichText(
        title=_("Speaker Biography (max. 1000 characters)"),
        max_length=1000,
        required=False,
    )

    # directives.write_permission(slides='cmf.ReviewPortalContent')
    slides = schema.URI(
        title=_("Vortragsfolien"),
        description=_("URL of the Website that holds the slides"),
        required=False,
    )

    directives.write_permission(video="cmf.ReviewPortalContent")
    video = schema.URI(
        title=_("Video"),
        description=_("URL of the Website that holds the video of the talk"),
        required=False,
    )

    directives.write_permission(hide_date="cmf.ReviewPortalContent")
    hide_date = schema.Bool(
        title=_("Hide date and time"),
        description=_("Display talks without date and time."),
        required=False,
        default=True,
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
        description=_(
            "Vortragsbeginn",
        ),
        # defaultFactory=get_default_start,
        required=False,
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
        description=_(
            "Vortragsende",
        ),
        # defaultFactory=get_default_start,
        required=False,
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


class Talk(Container):
    """Talk content type implementation"""
