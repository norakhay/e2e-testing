# e2e_testing

Simple e2e test for the live todo API at `https://todo.pixegami.io`. One test walks a full user flow over HTTP. Nothing is mocked.

## Setup

```bash
pip install -r requirements.txt
```

## How the tests are written

File: `test_e2e_todo.py`

1. Import `requests`.
2. Set `ENDPOINT` to the live API URL.
3. `PUT /create-task` and save `task_id`.
4. `GET /get-task/{task_id}` and `GET /list-tasks/{user_id}`.
5. `PUT /update-task`, then get again to confirm the change.
6. `DELETE /delete-task/{task_id}`, then get again and expect `404`.

Example:

```python
import requests

ENDPOINT = "https://todo.pixegami.io"

create_response = requests.put(
    f"{ENDPOINT}/create-task",
    json={"user_id": user_id, "content": content},
)
assert create_response.status_code == 200
task_id = create_response.json()["task"]["task_id"]
```

Needs internet.

## Run tests

```bash
pytest test_e2e_todo.py
```
