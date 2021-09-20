"""
    expected
    >>> buscar_avatar('gvanrossum')
    'https://avatars.githubusercontent.com/u/2894642?v=4'
"""
import requests


def buscar_avatar(username: str) -> str:
    """
    Busca o avatar de um usuário no Github
    :param username: str com o nome do usuário no Github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    return response.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('gvanrossum'))
