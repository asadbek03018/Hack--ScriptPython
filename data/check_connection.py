import requests

def test_connection(default = 'www.google.com') -> bool:
    try:
        get = requests.get(f"https://{default}/").text
        return True
    except requests.exceptions.ConnectionError:
        return False
