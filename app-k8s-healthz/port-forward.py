import subprocess
import time

def run_port_forward():
    command = ['kubectl', 'port-forward', 'svc/webcolor', '8080:80']
    process = subprocess.Popen(command)

    while True:
        if process.poll() is not None:
            # O processo terminou, então ocorreu um erro
            #print('Ocorreu um erro ao encaminhar a porta. Tentando novamente...')
            time.sleep(5)  # Aguardar 5 segundos antes de tentar novamente
            process = subprocess.Popen(command)
        
        time.sleep(1)  # Aguardar 1 segundo antes de verificar novamente

if __name__ == '__main__':
    run_port_forward()



