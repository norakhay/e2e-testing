from uuid import uuid4

import requests

ENDPOINT = "https://todo.pixegami.io"


def test_user_can_create_update_and_delete_a_task():
    user_id = f"user_{uuid4().hex}"
    content = f"e2e task {uuid4().hex}"

    create_response = requests.put(
        f"{ENDPOINT}/create-task",
        json={"user_id": user_id, "content": content},
    )
    assert create_response.status_code == 200
    task_id = create_response.json()["task"]["task_id"]

    get_response = requests.get(f"{ENDPOINT}/get-task/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["content"] == content

    list_response = requests.get(f"{ENDPOINT}/list-tasks/{user_id}")
    assert list_response.status_code == 200
    assert len(list_response.json()["tasks"]) == 1

    updated_content = f"updated e2e task {uuid4().hex}"
    update_response = requests.put(
        f"{ENDPOINT}/update-task",
        json={"task_id": task_id, "content": updated_content, "is_done": True},
    )
    assert update_response.status_code == 200

    updated = requests.get(f"{ENDPOINT}/get-task/{task_id}")
    assert updated.json()["content"] == updated_content
    assert updated.json()["is_done"] is True

    delete_response = requests.delete(f"{ENDPOINT}/delete-task/{task_id}")
    assert delete_response.status_code == 200

    missing = requests.get(f"{ENDPOINT}/get-task/{task_id}")
    assert missing.status_code == 404
