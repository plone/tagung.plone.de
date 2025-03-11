from plone import api
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


# from tagung.plone.de import _


@provider(IVocabularyFactory)
def RoomVocabulary(context):
    name = "ploneconf.room"
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)


@provider(IVocabularyFactory)
def TalkTypeVocabulary(context):
    name = "ploneconf.type_of_talk"
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)


@provider(IVocabularyFactory)
def AudienceVocabulary(context):
    name = "ploneconf.audience"
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)
