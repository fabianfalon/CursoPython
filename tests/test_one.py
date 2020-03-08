from unittest import TestCase, mock

from some_function import get_posts, hello


class TestOne(TestCase):

    def test_sum(self):
        data = [1, 2, 3, 4]
        result = sum(data)
        self.assertEqual(result, 10)

    def test_string(self):
        data = ("Fabian", "Pepe", "Juan", "Pedro")
        self.assertIn("Pepe", data)


class TestMockValue(TestCase):
    @mock.patch("some_function.get_greeting")
    def test_get_text(self, mocked_response):
        mocked_response.return_value = "mocked string"
        response = hello()
        self.assertEqual(response, "mocked string")


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
