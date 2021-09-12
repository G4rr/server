
# Librery for building user-data terraform file

def get_default_introduction():
    return '''sudo apt update -y
sudo apt install apt-transport-https -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update -y
sudo apt install docker-ce docker-ce-cli containerd.io -y
sudo systemctl status docker

sudo docker pull owasp/zap2docker-stable
sudo docker pull sullo/nikto
sudo docker pull cyberwatch/wapiti

    '''.format()

def get_setup_server():
    return '''
echo '#!/usr/bin/env python3
import socket
import os
HOST = "0.0.0.0"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print("Connection from", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            os.system(data)
        print("Closed")
' > server.py
python3 server.py
    '''.format()

def get_docker(option='', command='', c_option=''):
    return '''docker {0} {1} {2}
    '''.format(option, command, c_option)

def get_docker_pull(option='', image_name=''):
    return '''docker pull {0} {1}
    '''.format(option, image_name)

def get_decker_run(option='', image='', command='', arg=''):
    return '''docker run {0} {1} {2} {3}
    '''.format(option, image, command, arg)

def get_docker_compose(module_name, image_name, container_name, host_port, container_port, environment, restart, links):
    return '''
echo "
  {0}:
    image: {1}
    container_name: {2}
    ports:
        - {3}:{4}
    environment: {5}
    restart: {6}
    links: {7}
" > docker-compose.yml
'''.format(module_name, image_name, container_name, host_port, container_port, environment, restart, links)
