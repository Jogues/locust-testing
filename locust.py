import time
from locust import HttpUser, task, between

class RegisterEndpoint(HttpUser):
    wait_time = between(1, 10)

    @task
    def register_page(self):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        headers = {"content-type": "application/json"}
        response = self.client.post("api/register/", json=payload, headers=headers)
        assert response.status_code is 200, "Unexpected response code: " + response.status_code
 