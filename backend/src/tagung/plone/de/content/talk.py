from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from plone.autoform import directives as form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.app.z3cform.widget import LinkFieldWidget
from zope.interface import Interface

from tagung.plone.de import _

# from plone.supermodel import xmlSchema
# ITalkfromXML = xmlSchema('talk.xml')

class ITalk(model.Schema):
  """Talk content type schema"""

  details = RichText(
    title=_("Details"),
    description=_("Description of the talk in max 3000 characters"),
    required=True
  )

  audience = schema.Choice(
        title=_("Audience"), vocabulary="tagung.talk.audience", required=True
    )


class Talk(Container):
    """Talk content type implementation"""