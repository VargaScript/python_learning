import requests
import pygame

while True:
    def ask_method():
        try:
            catching_method = input("""How do you want to identify the Pokémon?
    1. Type '1' to identify it by number
    2. Type '2' to identify it by name
    
    Your choice: """).strip()

            if catching_method == '1':
                pokemon_by_id = int(input("Type the number of the Pokémon you want to hear: ").strip())
                return pokemon_by_id
            elif catching_method == '2':
                pokemon_by_name = input("Type the name of the Pokémon you want to hear: ").strip().lower()
                return pokemon_by_name
            else:
                raise ValueError("You must type '1' or '2'.")
        except ValueError as ve:
            print(f"Error: {ve}")
            return None

    def api_call(base_url="https://pokeapi.co/api/v2/pokemon"):
        identifier = ask_method()
        if not identifier:
            return None

        try:
            api_request = requests.get(f"{base_url}/{identifier}")
            api_request.raise_for_status()
            info = api_request.json()
            return info["cries"]["latest"]
        except requests.exceptions.RequestException as e:
            print(f"API error: {e}")
            return None
        except KeyError:
            print("The Pokémon exists but has no legacy cry.")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def download_sound(url: str, filename: str = "cry.ogg") -> str:
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename

    def produce_pokemon_sound(file_path: str):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    sound_url = api_call()
    if sound_url:
        local_file = download_sound(sound_url)
        produce_pokemon_sound(local_file)
