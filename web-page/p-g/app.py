from flask import Flask
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Contador para as requisições do serviço
requests_counter = Counter('my_app_requests_total', 'Total number of requests received')

# Medidor para a quantidade de memória usada
memory_usage = Gauge('my_app_memory_usage', 'Memory usage of the application')

# Histograma para a latência das requisições
request_latency = Histogram('my_app_request_latency_seconds', 'Latency of requests')

# Sumário para o tempo de resposta
response_time_summary = Summary('my_app_response_time_seconds', 'Response time summary')

# Registrador de exceção para contar o número de exceções lançadas
exception_counter = Counter('my_app_exceptions_total', 'Total number of exceptions')


@app.route('/metrics')
def metrics():
    requests_counter.inc()  # Incrementa o contador a cada requisição
    memory_usage.set(512)  # Define um valor fixo para o exemplo
    request_latency.observe(0.5)  # Observa um valor de latência para o exemplo
    response_time_summary.observe(0.2)  # Observa um valor de tempo de resposta para o exemplo
    exception_counter.inc()  # Incrementa o contador de exceções

    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route('/')
def index():
    return 'Hello World! 05/07/2023'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
