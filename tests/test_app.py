from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Testa se a rota raiz retorna a mensagem correta
    """
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_exercicio_ola_mundo_em_html():
    """
    Testa se o endpoint HTML retorna o conteúdo esperado
    """
    client = TestClient(app)
    response = client.get('/exercicio-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text

    # Código alternativo comentado:
    # response = client.get("/")
    # assert response.status_code == 200
    # assert response.json() == {"message": "Olá mundo!"}
