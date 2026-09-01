from pathlib import Path

from playwright.sync_api import expect

PAGE = (Path(__file__).parent / "index.html").as_uri()


def test_user_can_add_and_delete_a_task(page):
    page.goto(PAGE)

    page.get_by_label("Task").fill("buy milk")
    page.get_by_role("button", name="Add").click()
    expect(page.get_by_text("buy milk")).to_be_visible()

    page.get_by_role("button", name="Delete").click()
    expect(page.get_by_text("buy milk")).to_have_count(0)
