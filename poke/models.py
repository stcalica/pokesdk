from typing import Dict, List, Any, Optional
import requests

class NamedAPIResource: 
    def __init__(self, name: str, url:str, resource_type: Optional[str] = None):
        self.name = name 
        self.url = url
        self._full_data = None
    
    def _fetch_full_data(self) -> Dict[str, Any]:
        if self._full_data is None:
            try: 
                response = requests.get(self.url)
                response.raise_for_status()
                self._full_data = response.json()
                return self._full_data
            except:
                #TODO raise error fetching API call 
                raise Exception

    # Lazy load for a seamless experience 
    def __getattr__(self, item):
        if self._full_data is None: 
            self._fetch_full_data()
        if item in self._full_data:
            return self._full_data[item]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")
        
    def __repr__(self):
        return f"<NamedAPIResource name={self.name}, resource_type={self.resource_type}>"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], resource_type: Optional[str] = None) -> 'NamedAPIResource':
        return cls(name=data['name'], url=data['url'], resource_type=resource_type)
    
class PokemonAbility:
    def __init__(self, ability: NamedAPIResource, is_hidden: bool, slot: int):
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot

    def __repr__(self):
        return f"<PokemonAbility ability={self.ability.name}, is_hidden={self.is_hidden}, slot={self.slot}>"


class PokemonMove:
    def __init__(self, move: NamedAPIResource, version_group_details: Any):
        self.move = move
        self.version_group_details = version_group_details

    def __repr__(self):
        return f"<PokemonMove move={self.move.name}>"


class GenerationMove:
    def __init__(self, move: NamedAPIResource):
        self.move = move

    def __repr__(self):
        return f"<PokemonMove move={self.move.name}>"

class PokemonType:
    def __init__(self, slot: int, type_: NamedAPIResource):
        self.slot = slot
        self.type_ = type_

class GenerationType:
    def __init__(self, type_: NamedAPIResource):
        self.type_ = type_

    def __repr__(self):
        return f"<PokemonType slot={self.slot}, type={self.type_.name}>"

class PokemonSpecies:
    def __init__(self, species: NamedAPIResource):
        self.species = species

    def __repr__(self):
        return f"<PokemonSpecies name={self.species.name}>"

#TODO add other attributes 
class Pokemon:
    def __init__(
        self,
        id: int,
        name: str,
        abilities: List[Dict[str, Any]],
        types: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
        species: Dict[str, Any],
        weight: Optional[int] = None,
        height: Optional[int] = None,
        base_experience: Optional[int] = None,
        is_default: Optional[bool] = False,
        order: Optional[int] = None,
        location_area_encounters: Optional[int] = None
    ):
        self.id = id
        self.name = name
        self.weight = weight
        self.height = height
        self.base_experience = base_experience
        self.is_default = is_default
        self.order = order
        self.location_area_encounters = location_area_encounters

        self._raw_abilities = abilities
        self._raw_types = types
        self._raw_moves = moves
        self.species = NamedAPIResource.from_dict(species, resource_type="Species")

        self._abilities = None
        self._types = None
        self._moves = None

    @property
    def abilities(self) -> List[PokemonAbility]:
        if self._abilities is None:
            self._abilities = [
                PokemonAbility(
                    ability=NamedAPIResource.from_dict(ability['ability'], resource_type="Ability"),
                    is_hidden=ability['is_hidden'],
                    slot=ability['slot']
                )
                for ability in self._raw_abilities
            ]
        return self._abilities

    @property
    def types(self) -> List[PokemonType]:
        if self._types is None:
            self._types = [
                PokemonType(
                    slot=type_['slot'],
                    type_=NamedAPIResource.from_dict(type_['type'], resource_type="Type")
                )
                for type_ in self._raw_types
            ]
        return self._types

    @property
    def moves(self) -> List[PokemonMove]:
        if self._moves is None:
            self._moves = [
                PokemonMove(
                    move=NamedAPIResource.from_dict(move['move'], resource_type="Move"),
                    version_group_details=move['version_group_details']
                )
                for move in self._raw_moves
            ]
        return self._moves

    #NOTE: this is NOT a reflection on the API but possibly a way to manipulate the models we provide -- is this better DX or more confusing? 
    def create_ability(
        self,
        name: str,
        url: str, 
        is_hidden: bool = False,
        slot: int = 1
    ):
        self._raw_abilities.append(
            {
                "ability": {"name": name, "url": url},
                "is_hidden": is_hidden,
                "slot": slot
            }
        )
        self._abilities = None

    def __repr__(self):
        return f"<Pokemon name={self.name}, id={self.id}>"

class Generation:
    def __init__(
        self,
        id: int,
        name: str,
        abilities: List[Dict[str, Any]],
        types: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
        species: List[Dict[str, Any]],
        main_region: Dict[str, Any],
        version_groups: Dict[str, Any]
    ):
        self.id = id
        self.name = name
        self.main_region = main_region
        self.version_groups = version_groups

        self._raw_abilities = abilities
        self._raw_types = types
        self._raw_moves = moves
        self._raw_species = species

        self._abilities = None
        self._types = None
        self._moves = None
        self._species = None

    @property
    def abilities(self) -> List[PokemonAbility]:
        if self._abilities is None:
            self._abilities = [
                PokemonAbility(
                    ability=NamedAPIResource.from_dict(ability, resource_type="Ability"),
                    is_hidden=ability['is_hidden'],
                    slot=ability['slot']
                )
                for ability in self._raw_abilities
            ]
        return self._abilities

    @property
    def types(self) -> List[GenerationType]:
        if self._types is None:
            self._types = [
                GenerationType(
                    type_=NamedAPIResource.from_dict(type_, resource_type="Type")
                )
                for type_ in self._raw_types
            ]
        return self._types

    @property
    def moves(self) -> List[GenerationMove]:
        if self._moves is None:
            self._moves = [
                GenerationMove(
                    move=NamedAPIResource.from_dict(move, resource_type="Move")
                )
                for move in self._raw_moves
            ]
        return self._moves

    @property
    def species(self) -> List[PokemonSpecies]:
        if self._species is None:
            self._species = [
                PokemonSpecies(
                    species=NamedAPIResource.from_dict(species, resource_type="Species"),
                )
                for species in self._raw_species
            ]
        return self._species


    def __repr__(self):
        return f"<Generation name={self.name}, id={self.id}>"


