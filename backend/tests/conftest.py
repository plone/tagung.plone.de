from pytest_plone import fixtures_factory
from tagung.plone.de.testing import ACCEPTANCE_TESTING
from tagung.plone.de.testing import FUNCTIONAL_TESTING
from tagung.plone.de.testing import INTEGRATION_TESTING


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (ACCEPTANCE_TESTING, "acceptance"),
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)
