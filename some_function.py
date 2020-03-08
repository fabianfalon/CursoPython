import requests

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def hello():
    return get_greeting()


def get_greeting():
    return "Hola Mundo"


def get_posts():
    response = requests.get(POSTS_URL)
    if response.ok:
        return response
    else:
        return None
