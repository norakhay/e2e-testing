# e2e-testing

Playwright e2e test for a tiny todo page (`index.html`). It drives a real browser and follows a user flow: type a task, click Add, then click Delete.

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
```

## How the tests are written

File: `test_e2e_todo.py`

1. Import `expect` from `playwright.sync_api`.
2. Point Playwright at `index.html`.
3. Use the `page` fixture from `pytest-playwright` (a real browser tab).
4. `page.goto` the todo page.
5. Fill the Task box and click **Add**. Assert the task is on the page.
6. Click **Delete**. Assert the task is gone.

Example:

```python
from playwright.sync_api import expect

def test_user_can_add_and_delete_a_task(page):
    page.goto(PAGE)
    page.get_by_label("Task").fill("buy milk")
    page.get_by_role("button", name="Add").click()
    expect(page.get_by_text("buy milk")).to_be_visible()
```

This matches **Playwright** user-workflow e2e. No API, no mocks — just the browser and the page.

## Run tests

```bash
pytest test_e2e_todo.py
```
