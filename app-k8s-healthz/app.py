from flask import Flask, jsonify
import time
import threading

app = Flask(__name__)
stop_healthz = False

def stop_healthz_after_delay():
    global stop_healthz
    time.sleep(120)  # 3 minutos de atraso
    stop_healthz = True

@app.route('/')
def hello_world():
    return 'Olá, mundo!'

@app.route('/healthz')
def health_check():
    if stop_healthz:
        return '', 503  # Retorno 503 - Serviço Indisponível
    response = {
        'status': 'OK'
    }
    return jsonify(response), 200

if __name__ == '__main__':
    # Inicia a thread para parar o /healthz após o atraso de 3 minutos
    t = threading.Thread(target=stop_healthz_after_delay)
    t.start()
    app.run(host='0.0.0.0', port=5000)
