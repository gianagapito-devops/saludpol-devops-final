from main import app


def test_inicio():
    cliente = app.test_client()
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    datos = respuesta.get_json()
    assert datos["sistema"] == "SALUDPOL"
    assert datos["mensaje"] == "API DevOps operativa"


def test_consulta_reembolso():
    cliente = app.test_client()
    respuesta = cliente.get("/reembolsos/12345")

    assert respuesta.status_code == 200
    datos = respuesta.get_json()
    assert datos["solicitud_id"] == 12345
    assert datos["estado"] == "En evaluación"
