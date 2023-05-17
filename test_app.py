import unittest
from flask import Flask
from flask.testing import FlaskClient

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Olá mundo!')

if __name__ == '__main__':
    unittest.main()
