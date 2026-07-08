# SALUDPOL DevOps Final

Aplicacion web demostrativa para consultar el estado de una solicitud de reembolso.

Proyecto final del curso DevOps SALUDPOL 2026.

## Objetivo

Demostrar un flujo DevOps completo aplicando:

- Control de versiones con Git y GitFlow.
- Automatizacion CI/CD con GitHub Actions.
- Pruebas automaticas con pytest.
- Containerizacion con Docker.
- Escaneo de seguridad con Trivy.

## Estructura del proyecto

saludpol-devops-final/
├── main.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_main.py
└── .github/
    └── workflows/
        └── ci.yml

## Endpoints de la API

Ruta principal:

curl http://localhost:5000/

Consulta de reembolso:

curl http://localhost:5000/reembolsos/12345

## Ejecucion con Docker

Construir imagen:

docker build -t saludpol-devops-final:v1 .

Ejecutar contenedor:

docker run -d -p 5000:5000 --name saludpol-api saludpol-devops-final:v1

Verificar imagen:

docker images | grep saludpol-devops-final

## Pipeline CI/CD

El pipeline ejecuta los siguientes pasos:

1. Checkout del codigo.
2. Configuracion de Python.
3. Instalacion de dependencias.
4. Ejecucion de tests automaticos.
5. Construccion de imagen Docker.
6. Escaneo de seguridad con Trivy.

## Seguridad

El objetivo del escaneo con Trivy es validar que la imagen Docker no tenga vulnerabilidades criticas ni altas.
