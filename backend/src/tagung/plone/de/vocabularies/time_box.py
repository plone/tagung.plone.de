from plone import api
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory

# from tagung.plone.de import _


@provider(IVocabularyFactory)
def TimeBoxTypeVocabulary(context):
    name = "plonetagung.type_of_time_box"
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)
