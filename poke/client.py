import requests
from typing import Dict, Any
from .models import Pokemon, Generation, NamedAPIResource
from .exceptions import PokeAPIError, PokeAPINetworkError, PokeAPIResponseError
import json

class PokeClient: 

    BASE_URL = "https://pokeapi.co/api/v2/"

    def __init__(self):
        pass

    def _make_request(self, endpoint: str) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.ConnectionError as e:
            raise PokeAPINetworkError("Failed to connect to PokeAPI. Please check your network.") from e
        except requests.HTTPError as e:
            raise PokeAPIResponseError(response.status_code, f"Failed to fetch data from endpoint '{endpoint}'.") from e
        except requests.RequestException as e:
            raise PokeAPIError("An unexpected error occurred while making a request to PokeAPI.") from e

    def get_pokemon(self, identifier: str) -> Pokemon:
        data = self._make_request(f"pokemon/{identifier}/")
        return Pokemon(
        id=data["id"],
        name=data["name"],
        abilities=data["abilities"], 
        types=data["types"], 
        moves=data["moves"],  
        species=data["species"],   
        weight=data["weight"],
        height=data["height"],
        order=data["order"],
        location_area_encounters=data["location_area_encounters"],
        is_default=data["is_default"]
    )

    def get_generation(self, identifier: str) -> NamedAPIResource:
        data = self._make_request(f"generation/{identifier}/")
        return Generation(
       id=data["id"],
        name=data["name"],
        abilities=data["abilities"], 
        types=data["types"], 
        moves=data["moves"],  
        species=data["pokemon_species"],   #NOTE interesting case cause we do change the name here
        main_region=data["main_region"],
        version_groups=data["version_groups"]
        )
