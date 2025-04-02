import unittest

from plone.app.testing import TEST_USER_ID, setRoles

# from tagung.plone.de.testing import TAGUNG_PLONE_DE_FUNCTIONAL_TESTING
from tagung.plone.de.testing import TAGUNG_PLONE_DE_INTEGRATION_TESTING


class UpgradeStepIntegrationTest(unittest.TestCase):
    layer = TAGUNG_PLONE_DE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_upgrade_step(self):
        # dummy, add tests here
        self.assertTrue(True)


# class UpgradeStepFunctionalTest(unittest.TestCase):
#
#     layer = TAGUNG_PLONE_DE_FUNCTIONAL_TESTING
#
#     def setUp(self):
#         self.portal = self.layer['portal']
#         setRoles(self.portal, TEST_USER_ID, ['Manager'])
