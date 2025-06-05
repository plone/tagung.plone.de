import pytest
from playwright.sync_api import expect
from plone.app.testing.interfaces import (
    TEST_USER_NAME,
    TEST_USER_PASSWORD,
)


class TestPwEvents:
    @pytest.fixture(autouse=True)
    def setup(self, portal_factory, playwright_page_factory):
        self.page = playwright_page_factory(
            username=TEST_USER_NAME, password=TEST_USER_PASSWORD
        )
        self.portal = portal_factory(
            username=TEST_USER_NAME, roles=["Member", "Contributor"]
        )
        self.plone_url = self.portal.absolute_url()

    def test_events_listing(self) -> None:
        # page.pause()
        page = self.page
        page.goto(f"{self.plone_url}")
        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Folder", exact=True).hover()
        page.screenshot(path="screens/add_folder_events.png")
        page.get_by_role("link", name="Folder", exact=True).click()
        # page.pause()
        page.locator("[name='form.widgets.IDublinCore.title']").click()
        page.locator("[name='form.widgets.IDublinCore.title']").fill("Events")
        page.screenshot(path="screens/fillin_folder_events_data.png")
        page.get_by_role("button", name="Save").click()
        expect(page.locator("ol")).to_contain_text("Events")
        page.screenshot(path="screens/folder_events.png")

        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Collection").hover()
        page.screenshot(path="screens/add_collection.png")
        page.get_by_role("link", name="Collection").click()

        page.get_by_role("textbox", name="Title •").click()
        page.get_by_role("textbox", name="Title •").fill("Events aggregator")
        page.get_by_role("link", name="Select criteria").click()
        page.locator(".select2-option-portal-type").click()
        page.get_by_role("group", name="Default").get_by_role("list").click()
        page.get_by_role("option", name="Event").click()
        page.get_by_role("link", name="Select criteria").click()
        page.get_by_role("option", name="Event end date").click()
        page.get_by_role("link", name="Before date").click()
        page.get_by_role("option", name="After today").click()
        page.get_by_role("link", name="No sorting").click()
        page.get_by_role("option", name="Event start date").click()
        page.screenshot(path="screens/fillin_collection_data.png")
        page.get_by_role("button", name="Save").click()
        expect(page.locator("ol")).to_contain_text("Events aggregator")

        page.locator("#portal-globalnav").get_by_role(
            "link", name="Events", exact=True
        ).click()
        expect(page.locator("#content-core > .entries > *")).to_have_count(1)
        page.screenshot(path="screens/collection_news_contains_one_item.png")

        page.get_by_role("link", name="Display").click()
        page.get_by_role("link", name="Select a content item as").focus()
        page.screenshot(path="screens/set_default_page.png")
        page.get_by_role("link", name="Select a content item as").click()
        page.screenshot(path="screens/set_default_page_to_events_collection.png")
        page.get_by_role("button", name="Save").click()
        page.screenshot(path="screens/set_default_page_to_events_collection2.png")

        page.locator("#portal-globalnav").get_by_role(
            "link", name="Events", exact=True
        ).click()
        expect(page.locator("#content-core > p")).to_contain_text(
            "No results were found."
        )

        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Event", exact=True).click()
        page.get_by_role("textbox", name="Title").click()
        page.get_by_role("textbox", name="Title").fill("Plone-Tagung 2025 in Koblenz")
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.start"]').click()
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.start"]').fill(
            "2025-06-10T13:00"
        )
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.end"]').click()
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.end"]').fill(
            "2025-06-12T16:30"
        )
        page.get_by_role("button", name="Save").click()
        expect(page.locator("h1")).to_contain_text("Plone-Tagung 2025 in Koblenz")

        page.get_by_label("breadcrumb").get_by_role("link", name="Events").click()

        page.get_by_role("link", name="Add new…").click()
        page.get_by_role("link", name="Event", exact=True).click()
        page.get_by_role("textbox", name="Title").click()
        page.get_by_role("textbox", name="Title").fill(
            "Plone Conference 2025 - Jyväskylä / Finland"
        )
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.start"]').click()
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.start"]').fill(
            "2025-10-13T13:00"
        )
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.end"]').click()
        page.locator('input[name="form\\.widgets\\.IEventBasic\\.end"]').fill(
            "2025-10-19T14:00"
        )
        page.get_by_text("Whole Day", exact=True).click()
        page.get_by_role("button", name="Save").click()
        expect(page.locator("h1")).to_contain_text(
            "Plone Conference 2025 - Jyväskylä / Finland"
        )

        page.get_by_label("breadcrumb").get_by_role("link", name="Events").click()
        # page.pause()
        expect(page.locator("#content-core > .entries > *")).to_have_count(2)

        page.get_by_role("link", name="Display").click()
        page.locator("#plone-contentmenu-display-event_listing").click()

        expect(page.locator("h1")).to_contain_text("Future events")
        expect(page.locator("#content-core")).to_contain_text(
            "Plone Conference 2025 - Jyväskylä / Finland"
        )
        expect(page.locator("#content-core")).to_contain_text(
            "Plone-Tagung 2025 in Koblenz"
        )

        expect(page.locator("#content-core .cal_month").nth(0)).to_contain_text("June")
        expect(page.locator("#content-core .cal_day").nth(0)).to_contain_text("10")
        expect(page.locator("#content-core .cal_wkday").nth(0)).to_contain_text(
            "Tuesday"
        )

        expect(page.locator("#content-core .cal_month").nth(1)).to_contain_text(
            "October"
        )
        expect(page.locator("#content-core .cal_day").nth(1)).to_contain_text("13")
        expect(page.locator("#content-core .cal_wkday").nth(1)).to_contain_text(
            "Monday"
        )

        expect(page.locator("#content-core > section > *")).to_have_count(2)
