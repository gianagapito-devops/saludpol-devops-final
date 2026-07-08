from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def inicio():
    return jsonify({
        "sistema": "SALUDPOL",
        "mensaje": "API DevOps operativa"
    })

@app.get("/reembolsos/<int:solicitud_id>")
def consultar_reembolso(solicitud_id):
    return jsonify({
        "solicitud_id": solicitud_id,
        "estado": "En evaluación",
        "mensaje": "Consulta demostrativa de reembolso"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
