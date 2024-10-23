import requests
import pytest

def test_berry_attributes():
    url = f"https://pokeapi.co/api/v2/berry/2"
    response = requests.get(url)
    
    # Verificar que la solicitud fue exitosa
    assert response.status_code == 200, f"Error: {response.status_code}"

    data = response.json()

def get_berry_data(berry_id):
    url = f"https://pokeapi.co/api/v2/berry/2"
    response = requests.get(url)
    response.raise_for_status()  # Lanza un error si la solicitud falla
    return response.json()

def test_berry_attributes():
    # Obtener datos de berry/1
    berry1 = get_berry_data(1)
    
    # Obtener datos de berry/2
    berry2 = get_berry_data(2)
    
    # Verificar que el name en firmness de berry/2 sea 'super-hard'
    assert berry2['firmness']['name'] == "super-hard", "El nombre de firmness no es 'super-hard'."
    
    # Verificar que el size de berry/2 sea mayor que el de berry/1
    assert berry2['size'] > berry1['size'], "El tamaño de berry/2 no es mayor que el de berry/1."
    
    # Verificar que el soil_dryness de berry/2 sea igual al de berry/1
    assert berry2['soil_dryness'] == berry1['soil_dryness'], "El soil_dryness de berry/2 no es igual al de berry/1"
    
    print("Todas las verificaciones pasaron.")
    
if __name__ == "__main__":
    pytest.main()
    
    
