from program import app
import unittest


class FlaskTest(unittest.TestCase):

    def test_empty_path(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)


if __name__ == '__main__':
    unittest.main()