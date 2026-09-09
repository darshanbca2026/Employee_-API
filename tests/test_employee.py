from unittest.mock import Mock
import crud
def test_get_employee_mock():

    fake_db = Mock()

    fake_employee = Mock()
    fake_employee.id = 1
    fake_employee.name = "Darshan"
    fake_employee.age = 22

    fake_db.query.return_value.filter.return_value.first.return_value = fake_employee

    result = crud.get_employee(fake_db, 1)

    assert result.id == 1
    assert result.name == "Darshan"
    assert result.age == 22
    
def test_create_employee_with_token(client, token):
    response = client.post(
        "/employees",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Darshan",
            "age": 22,
            "department": "IT"
        }
    )
    assert response.status_code == 200
def test_get_employee(client, token):
    response = client.get(
        "/employees/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
def test_get_employee_not_found(client, token):
    response = client.get(
        "/employees/99999",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404
def test_create_employee_without_token(client):

    response = client.post(
        "/employees",
        json={
            "name": "Darshan",
            "age": 22,
            "department": "IT"
        }
    )

    assert response.status_code == 401
def test_update_employee(client, token):

    response = client.put(
        "/employees/1",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Updated Name",
            "age": 23,
            "department": "HR"
        }
    )
def test_update_employee_not_found(client, token):
    response = client.put(
        "/employees/99999",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name": "Test Employee",
            "age": 25
        }
    )

    assert response.status_code == 404
def test_delete_employee(client, token):

    response = client.delete(
        "/employees/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
def test_delete_employee_not_found(client, token):
    response = client.delete(
        "/employees/99999",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404
    