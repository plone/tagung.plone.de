from tagung.plone.de.content.time_box import ITimeBox  # NOQA E501
from tagung.plone.de.testing import TAGUNG_PLONE_DE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class TimeBoxIntegrationTest(unittest.TestCase):
    layer = TAGUNG_PLONE_DE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_time_box_schema(self):
        fti = queryUtility(IDexterityFTI, name="Time Box")
        schema = fti.lookupSchema()
        self.assertEqual(ITimeBox, schema)

    def test_ct_time_box_fti(self):
        fti = queryUtility(IDexterityFTI, name="Time Box")
        self.assertTrue(fti)

    def test_ct_time_box_factory(self):
        fti = queryUtility(IDexterityFTI, name="Time Box")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITimeBox.providedBy(obj),
            "ITimeBox not provided by {}!".format(
                obj,
            ),
        )

    def test_ct_time_box_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Time Box",
            id="time_box",
        )

        self.assertTrue(
            ITimeBox.providedBy(obj),
            "ITimeBox not provided by {}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("time_box", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("time_box", parent.objectIds())

    def test_ct_time_box_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Time Box")
        self.assertTrue(fti.global_allow, f"{fti.id} is not globally addable!")
