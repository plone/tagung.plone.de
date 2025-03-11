from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel import model
from tagung.plone.de import _
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema


class ITalk(model.Schema):
    """Talk content type schema"""

    directives.widget(type_of_talk=RadioFieldWidget)
    type_of_talk = schema.Choice(
        title=_("Type of talk"),
        vocabulary="tagung.talk.type_of_talk",
        required=True,
        max_length=3000,
    )

    details = RichText(
        title=_("Details"),
        description=_("Description of the talk (max. 3000 characters)"),
        max_length=3000,
        required=True,
    )

    directives.widget(audience=CheckBoxFieldWidget)
    directives.write_permission(audience="cmf.ReviewPortalContent")
    audience = schema.Set(
        title=_("Audience"),
        value_type=schema.Choice(
            vocabulary="ploneconf.audience",
        ),
        required=False,
    )

    directives.write_permission(room="cmf.ReviewPortalContent")
    room = schema.Choice(
        title=_("Room"),
        vocabulary="ploneconf.room",
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

    twitter = schema.TextLine(
        title=_("Twitter name"),
        required=False,
    )

    github = schema.TextLine(
        title=_("Github username"),
        required=False,
    )

    # image = NamedBlobImage(
    #     title=_(u'Image'),
    #     description=_(u'Portrait of the speaker'),
    #     required=False,
    #     )

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


class Talk(Container):
    """Talk content type implementation"""
