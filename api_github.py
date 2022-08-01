import unittest

def get_username(username: str) -> dict:
    ...

class User:
    ...

class TestMethods(unittest.TestCase):
    """Classe de testes unitários. Crie seus testes aqui."""

    def test_this_test_words(self):
        self.assertTrue(True)

    def test_username_parameters(self):
        parameters = ['login', 'id', 'avatar_url', 'html_url']
        response = get_username('githubuser')
        for param in parameters:
            self.assertTrue(param in response.keys())

    def test_user_object(self):
        ...

if __name__ == "__main__":
    unittest.main()