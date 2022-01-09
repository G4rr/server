
# Librery for building user-data terraform file

def get_default_introduction():
    return '''sudo apt update -y
sudo apt install apt-transport-https -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update -y
sudo apt install docker-ce docker-ce-cli containerd.io -y

sudo docker pull owasp/zap2docker-stable
sudo docker pull olexii21/nikto
sudo docker pull olexii21/wapiti
    '''.format()

def get_docker(option='', command='', c_option=''):
    return '''docker {0} {1} {2}
    '''.format(option, command, c_option)

def get_docker_pull(option='', image_name=''):
    return '''docker pull {0} {1}
    '''.format(option, image_name)

def get_decker_run(option='', image='', command='', arg=''):
    return '''docker container run {0} {1} {2} {3}
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
