import requests
import threading

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

def run_stress_test(url, num_requests):
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_url = "http://a501fe7cd84924ee39de7cc0943fc2e0-1264494035.us-east-1.elb.amazonaws.com/"  # URL do servidor a ser testado
    num_requests = 100000  # Número de requisições a serem enviadas

    run_stress_test(target_url, num_requests)
