import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Create test client
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "healthy")

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "Hello, CI/CD!")

if __name__ == '__main__':
    unittest.main()
