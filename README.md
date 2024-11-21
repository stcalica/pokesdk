# **PokeAPI SDK**

A Python SDK for accessing Pokémon data from [PokeAPI](https://pokeapi.co). 

## **Installation**

### **Prerequisites**
- Python 3.11
- `pip` for dependency management

### **Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pokeapi-sdk.git
   cd pokesdk
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify the installation by running the test script:
   ```bash
   pytest
   ```

## **Usage**

### **1. Initialize the Client**
The `PokeClient` is your gateway to interacting with the PokeAPI.

```python
from poke.client import PokeClient

client = PokeClient()
```

### **2. Fetch a Pokémon by Name or ID**
Retrieve details about a Pokémon, including its abilities, types, and moves.

```python
clefairy = client.get_pokemon("clefairy")
print(f"Pokemon Name: {clefairy.name}")
print(f"Abilities: {[ability.ability.name for ability in clefairy.abilities]}")
```

### **3. Fetch a Generation by Name or ID**
Get details about a specific Pokémon generation.

```python
gen1 = client.get_generation(1)
print(f"Generation Name: {gen1.name}")
```

### **4. Handle Errors Gracefully**
The SDK raises custom exceptions for common errors:
- `PokeAPINetworkError`: Network-related issues
- `PokeAPIResponseError`: Issues with API responses (e.g., 404 Not Found)
- `PokeAPIError`: General errors

```python
try:
    pikachu = client.get_pokemon("pikachu")
except PokeAPIError as e:
    print(f"An error occurred: {e}")
```

---

## **Testing**

### **Run the Test Script**
A simple test script is provided in the `/tests` folder. To run it:
```bash
pytest
```

## **Design Decisions for Developer Experience**

### **Critical Design Features**
1. **Lazy Loading with `NamedAPIResource`**:
   - Related resources (e.g., abilities, moves) are fetched only when accessed.
   - Improves performance by reducing unnecessary API calls.

2. **Custom Exceptions**:
   - `PokeAPINetworkError`, `PokeAPIResponseError`, and `PokeAPIError` make error handling intuitive and meaningful for developers.
   - Prevents exposing raw URLs or internal API details, improving security and clarity.

3. **Modular Code Structure**:
   - The project is split into separate files for the client, models, and exceptions, making it easier to maintain and extend.
