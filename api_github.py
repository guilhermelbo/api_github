import unittest
import requests

def get_username(username: str) -> dict:
    username = requests.get('https://api.github.com/users/'+username)
    return username.json()

class User:
    def __init__(self, user_data):
        self.id = user_data['id']
        self.login = user_data['login']
        self.avatar_url = user_data['avatar_url']
        self.html_url = user_data['html_url']
        self.name = user_data['name']
        self.bio = user_data['bio']
        self.email = user_data['email']
    
    def get_field(self, name):
        return getattr(self, name)


class TestMethods(unittest.TestCase):
    """Classe de testes unitários. Crie seus testes aqui."""

    def test_this_test_words(self):
        self.assertTrue(True)

    def test_username_parameters(self):
        parameters = ['login', 'id', 'avatar_url', 'html_url']
        response = get_username('guilhermelbo')
        for param in parameters:
            self.assertTrue(param in response.keys())

    def test_user_object(self):
        username = get_username('guilhermelbo')
        user = User(username)
        parameters = ['id', 'login', 'avatar_url', 'html_url', 'name', 'bio', 'email']
        for param in parameters:
            self.assertEqual(user.get_field(param), username[param])

if __name__ == "__main__":
    unittest.main()