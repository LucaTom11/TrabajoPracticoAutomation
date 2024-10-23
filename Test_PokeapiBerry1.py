import requests
import pytest

def test_berry_attributes():
    url = "https://pokeapi.co/api/v2/berry/1"
    response = requests.get(url)

    # Verificar que la solicitud fue exitosa
    assert response.status_code == 200, f"Error: {response.status_code}"

    data = response.json()

# Verificar que el size sea 20
def test_size(berry_data):
    assert berry_data['size'] == 20, "El tamaño no es 20."

# Verificar que el soil_dryness sea 15
def test_soil_dryness(berry_data):
    assert berry_data['soil_dryness'] == 15, "El soil_dryness no es 15."

# Verificar que en firmness, el name sea soft
def test_firmness_name(berry_data):
    assert berry_data['firmness']['name'] == "soft", "El nombre de firmness no es 'soft'."

if __name__ == "__main__":
    pytest.main()


    print("Todas las verificaciones pasaron.")

if __name__ == "__main__":
    test_berry_attributes()
