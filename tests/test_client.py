from poke.client import PokeClient 
from poke.models import NamedAPIResource, PokemonAbility

def test_poke_client():
    client = PokeClient()
    assert client is not None 

def test_fetch_pokemon():
    client = PokeClient()
    charmander = client.get_pokemon('charmander')
    assert charmander is not None
    assert charmander.name == 'charmander'
    assert charmander.id is not None
    assert charmander.height is not None
    assert charmander.weight is not None
    assert charmander.order is not None
    assert charmander.is_default is not None
    assert charmander.location_area_encounters is not None


def test_fetch_abilities():
    client = PokeClient()
    charmander = client.get_pokemon('charmander')
    assert charmander.abilities is not None

def test_fetch_moves():
    client = PokeClient()
    charmander = client.get_pokemon('charmander')
    assert charmander.moves is not None

def test_fetch_types():
    client = PokeClient()
    charmander = client.get_pokemon('charmander')
    assert charmander.types is not None

def test_fetch_species():
    client = PokeClient()
    charmander = client.get_pokemon('charmander')
    assert charmander.species is not None

def test_fetch_generation():
    client = PokeClient()
    generation = client.get_generation(1)
    assert generation is not None
    assert generation.name is not None
    assert generation.id is not None
    assert generation.moves is not None
    assert generation.types is not None
    assert generation.species is not None
    assert generation.main_region is not None
    assert generation.abilities is not None

def test_fetch_generation():
    client = PokeClient()
    generation = client.get_generation(1)
    assert generation is not None
    assert generation.name is not None
    assert generation.id is not None
    assert generation.moves is not None
    assert generation.types is not None
    assert generation.species is not None
    assert generation.main_region is not None
    assert generation.abilities is not None

#NOTE: example of using the models for additonal creation
def test_change_pokemon_data():
    client = PokeClient()
    charmander = client.get_pokemon('charmander')
    charmander.name = 'fire spirit'
    fly_resource = NamedAPIResource(name='fly', url='fake')
    fly = PokemonAbility(is_hidden=True, slot=7, ability=fly_resource )
    charmander.abilities.append(fly)
    assert charmander.name == 'fire spirit'
    assert charmander.abilities[-1] is fly
    
#NOTE testing our very experimental method for changing abilities 
def test_create_pokemon_ability():
    client = PokeClient()
    charmander = client.get_pokemon('charmander')
    charmander.create_ability('fly', 'https://fake.com')
