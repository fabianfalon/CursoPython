from unittest import TestCase, mock
from some_function import get_posts, hello, Calculadora


class TestMockValue(TestCase):
    @mock.patch("some_function.get_greeting")
    def test_get_text(self, mocked_response):
        mocked_response.return_value = "mocked string"
        response = hello()
        self.assertEqual(response, "mocked string")

    @mock.patch.object(Calculadora, "suma")
    def test_calculadora(self, mock_method):
        mock_method.return_value = 10
        calculadora = Calculadora()
        result = calculadora.suma(5, 2)
        self.assertEqual(10, result)


class TestGetPost(TestCase):
    @mock.patch("requests.get")  # Mock requests module get
    def test_blog_posts(self, mock_get):
        expected = [
            {
                "userId": 1,
                "id": 1,
                "title": "Test Title",
                "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam viverra convallis ex, et vehicula nulla ultrices.",
            },
            {
                "userId": 1,
                "id": 2,
                "title": "Test Title 2",
                "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam viverra convallis ex, et vehicula nulla ultrices.",
            }
        ]

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected
        response = get_posts()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)
