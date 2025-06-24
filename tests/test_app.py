from fastapi.testclient import TestClient
from fastapi_zero.app import app
from http import HTTPStatus  # Para evitar magic numbers

def test_root_deve_retornar_ola_mundo():
    """  
    Testa se a rota raiz retorna a mensagem correta  
    """  

    # Arrange: configuração inicial  
    client = TestClient(app)

    # Act: chamada à API
    response = client.get('/')

    # Assert: verificações
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}  # Corrigido "01á" para "Olá"
# def test_read_root():
   # response = client.get("/")
    #assert response.status_code == 200
    #assert response.json() == {"message": "Olá mundo!"}
