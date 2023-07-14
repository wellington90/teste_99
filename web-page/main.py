import subprocess
import time

def check_port_forward():
    process = subprocess.Popen(['kubectl', 'port-forward', 'deployment/web-page', '8080:80'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    time.sleep(5)

    if process.poll() is None:
        print("Port-forward is running")
        return True
    else:
        print("Port-forward is not running")
        return False

def restart_port_forward():
    
    time.sleep(5)
    subprocess.call(['kubectl', 'port-forward', 'deployment/web-page', '8080:80'])

while True:
    if not check_port_forward():
        print("Restarting port-forward")
        restart_port_forward()

    time.sleep(15)
