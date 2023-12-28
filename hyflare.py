import requests

class Hyflare:
    def __init__(self):
        self.base_url = 'https://api.hyflare.net'

    def get_player_data(self, username):
        endpoint = f"{self.base_url}/player"
        params = {'username': username}
        response = requests.get(endpoint, params=params)
        return response.json()

    def get_ranks(self):
        endpoint = f"{self.base_url}/ranks"
        response = requests.get(endpoint)
        return response.json()

    def get_server_player_count(self):
        endpoint = f"{self.base_url}/count"
        response = requests.get(endpoint)
        return response.json()