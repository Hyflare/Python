from hyflare import Hyflare


if __name__ == '__main__':
    minecraft_api = Hyflare()

    # Example usage
    username = 'xdskyblock'
    player_data = minecraft_api.get_player_data(username)
    print(f"Player Data for {username}:", player_data)

    ranks_data = minecraft_api.get_ranks()
    print("List of Ranks:", ranks_data)

    server_player_count = minecraft_api.get_server_player_count()
    print("Server Player Count:", server_player_count)
