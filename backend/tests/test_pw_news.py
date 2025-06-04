import pytest
from playwright.sync_api import expect
from plone.app.testing.interfaces import (
    TEST_USER_NAME,
    TEST_USER_PASSWORD,
)


class TestPwNews:
    @pytest.fixture(autouse=True)
    def setup(self, portal_factory, playwright_page_factory) -> None:
        self.portal = portal_factory(username=TEST_USER_NAME, roles=["Contributor"])
        self.page = playwright_page_factory(
            username=TEST_USER_NAME, password=TEST_USER_PASSWORD
        )
        self.plone_url = self.portal.absolute_url()

    def test_news_listing(self) -> None:
        page = self.page
        page.goto(f"{self.plone_url}")
        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Folder", exact=True).click()
        page.locator("[name='form.widgets.IDublinCore.title']").click()
        page.locator("[name='form.widgets.IDublinCore.title']").fill("News")
        page.get_by_role("button", name="Save").click()
        expect(page.locator("ol")).to_contain_text("News")

        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Collection").click()
        page.get_by_role("textbox", name="Title •").click()
        page.get_by_role("textbox", name="Title •").fill("News aggregator")
        page.get_by_role("link", name="Select criteria").click()
        page.locator(".select2-option-portal-type").click()
        page.get_by_role("group", name="Default").get_by_role("list").click()
        page.get_by_role("option", name="News item").click()
        page.get_by_role("link", name="No sorting").click()
        page.get_by_role("option", name="Effective date").click()
        page.get_by_role("checkbox").check()
        page.get_by_role("button", name="Save").click()
        expect(page.locator("ol")).to_contain_text("News aggregator")
