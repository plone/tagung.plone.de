# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from tagung.plone.de import _


class ISponsor(model.Schema):
    """Marker interface and Dexterity Python Schema for Sponsor"""

    level = schema.Choice(
        title=_(
            "Level",
        ),
        description=_(
            "",
        ),
        vocabulary="tagung.plone.de.Levels",
        default="Organizer",
        # defaultFactory=get_default_level,
        required=True,
        readonly=False,
    )

    # Make sure you import: plone.namedfile.field as namedfile
    logo = namedfile.NamedBlobImage(
        title=_(
            "Logo",
        ),
        description=_(
            "",
        ),
        required=True,
        readonly=False,
    )

    link = schema.URI(
        title=_(
            "Link",
        ),
        description=_(
            "",
        ),
        default="https://",
        required=False,
        readonly=False,
    )


@implementer(ISponsor)
class Sponsor(Container):
    """Content-type class for ISponsor"""
