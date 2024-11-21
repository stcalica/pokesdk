# **PokéSDK**

PokéSDK is a Python SDK designed to simplify interactions with the [PokéAPI](https://pokeapi.co), enabling developers to effortlessly access and manage Pokémon data.

---

## **Installation**

### **Prerequisites**

- Python 3.11 or higher
- `pip` for dependency management

### **Steps**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/stcalica/pokesdk.git
   cd pokesdk
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation:**

   ```bash
   pytest
   ```

---

## **Usage**

### **1. Initialize the Client**

```python
from poke.client import PokeClient

client = PokeClient()
```

### **2. Fetch Pokémon Details**

Retrieve information about a specific Pokémon:

```python
clefairy = client.get_pokemon("clefairy")
print(f"Pokémon Name: {clefairy.name}")
print(f"Abilities: {[ability.ability.name for ability in clefairy.abilities]}")
```

### **3. Fetch Generation Details**

Retrieve information about a specific Pokémon generation:

```python
gen1 = client.get_generation(1)
print(f"Generation Name: {gen1.name}")
```

### **4. Handle Errors**

The SDK raises custom exceptions for error handling:

```python
try:
    pikachu = client.get_pokemon("pikachu")
except PokeAPIError as e:
    print(f"An error occurred: {e}")
```

---

## **Testing**

To run the test suite:

```bash
pytest
```

Ensure all tests pass to confirm the SDK is functioning correctly.

---

## **Design Decisions for Developer Experience**

### **1. Lazy Loading with `NamedAPIResource`**

- Related resources (e.g., abilities, moves) are fetched only when accessed, reducing unnecessary API calls and improving performance.

### **2. Custom Exceptions**

- The SDK defines specific exceptions (`PokeAPIError`, `PokeAPINetworkError`, `PokeAPIResponseError`) to provide clear and meaningful error messages, enhancing the developer experience.

### **3. Modular Structure**

- The codebase is organized into distinct modules (`client`, `models`, `exceptions`) to promote maintainability and scalability.


## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.
