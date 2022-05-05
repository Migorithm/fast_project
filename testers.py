import unittest
from fastapi.testclient import TestClient
from main import app

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def tearDown(self) -> None:
        self.client.cookies.clear()
    
    def test_login_get(self):
        response = self.client.get("/login")
        self.assertEqual(200,response.status_code)
        

    def test_login_post(self):
        response = self.client.post("/login", data = {"username":"migo","password":"admin1234"})
        self.assertEqual(302,response.status_code)

    def test_unauthenticated(self):
        response = self.client.post("/login", data = {"username":"migo","password":"admin1234"})
        self.assertEqual(302,response.status_code)

        response = self.client.get("/login/test")
        self.assertEqual(200,response.status_code)


if __name__ =="__main__":
    unittest.main()