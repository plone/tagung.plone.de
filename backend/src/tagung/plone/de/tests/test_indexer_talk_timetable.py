from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from tagung.plone.de.testing import TAGUNG_PLONE_DE_FUNCTIONAL_TESTING
from tagung.plone.de.testing import TAGUNG_PLONE_DE_INTEGRATION_TESTING

import unittest


class IndexerIntegrationTest(unittest.TestCase):
    layer = TAGUNG_PLONE_DE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_dummy(self):
        self.assertTrue(True)


class IndexerFunctionalTest(unittest.TestCase):
    layer = TAGUNG_PLONE_DE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_dummy(self):
        self.assertTrue(True)
