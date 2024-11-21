from poke.client import PokeClient

clefairy = client.get_pokemon("clefairy")
print(f"Pokemon Name: {clefairy.name}")
print(f"Abilities: {[ability.ability.name for ability in clefairy.abilities]}")
