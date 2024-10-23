import requests
import pytest

# Obtener datos de Pokémon por nombre
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)
    response.raise_for_status()  # si falla la solicitud tira error
    return response.json()

def test_pikachu_attributes():
    # Obtener datos de Pikachu
    pikachu = get_pokemon_data("pikachu")
    print(pikachu)  # Imprimir datos para ver la respuesta

    # Verificar que su experiencia base esté entre 10 y 1000
    base_experience = pikachu['base_experience']
    assert 10 < base_experience < 1000, "La experiencia base no está en el rango esperado (10, 1000)."

    # Verificar que su tipo sea "electric"
    types = [t['type']['name'] for t in pikachu['types']]
    assert "electric" in types, "Pikachu no es de tipo 'electric'."

    print("Todas las verificaciones pasaron.")

if __name__ == "__main__":
    pytest.main()





