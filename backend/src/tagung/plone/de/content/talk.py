from plone.app.textfield import RichText
from plone.autoform import directives as form
from plone.dexterity.content import Container
from plone.schema import email
from plone.supermodel import model
from tagung.plone.de import _
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema


# from plone.supermodel import xmlSchema
# ITalkfromXML = xmlSchema('talk.xml')


class ITalk(model.Schema):
    """Talk content type schema"""

    details = RichText(
        title=_("Details"),
        description=_("Description of the talk in max 3000 characters"),
        required=True,
        max_length=3000,
    )

    form.widget(audience=CheckBoxFieldWidget)
    audience = schema.List(
        title=_("Audience"),
        description=_("Audience of the talk"),
        required=False,
        value_type=schema.Choice(vocabulary="tagung.talk.audience"),
    )

    speaker = schema.TextLine(
        title=_("Speaker"),
        description=_("Name(s) of the speaker"),
        required=True,
    )
    organisation = schema.TextLine(
        title=_("Organisation"),
        required=False,
    )
    email = email.Email(
        title=_("E-Mail"),
        description=_("Email Address of the speaker"),
        required=False,
    )
    website = schema.URI(
        title=_("Website"),
        description=_("Website of the speaker"),
        required=False,
    )
    twitter = schema.TextLine(
        title=_("Twitter"),
        description=_("Twitter handle of the speaker"),
        required=False,
    )
    speaker_bio = RichText(
        title=_("Speaker Bio"),
        description=_("Biography of the speaker"),
        required=False,
        max_length=3000,
    )
    slides = schema.URI(
        title=_("Slides"),
        description=_("Link to the slides"),
        required=False,
    )
    form.write_permission(video="cmf.ManagePortal")
    video = schema.URI(
        title=_("Video"),
        description=_("Link to the video"),
        required=False,
    )
    form.write_permission(hide_date="cmf.ManagePortal")
    hide_date = schema.Bool(
        title=_("Hide Date and Time"),
        description=_("Display talks without date and time."),
        required=False,
    )


class Talk(Container):
    """Talk content type implementation"""
