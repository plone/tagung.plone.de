from tagung.plone.de import _
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def audience_vocabulary(context) -> SimpleVocabulary:
    return SimpleVocabulary(
        [
            SimpleTerm(value="beginner", title=_("Beginner")),
            SimpleTerm(value="developer", title=_("Developer")),
            SimpleTerm(value="expert", title=_("Expert")),
            SimpleTerm(value="integrator", title=_("Integrator")),

        ]
    )
