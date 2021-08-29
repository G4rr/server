
# Librery for building user-data terraform file

def get_default_introduction():
    return '''
sudo apt update -y
sudo apt install apt-transport-https -y
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update -y
sudo apt install docker-ce docker-ce-cli containerd.io -y
sudo systemctl status docker
sudo usermod -aG docker $USER
    '''.format()

def get_docker(option='', command='', c_option=''):
    return '''
docker {0} {1} {2}
    '''.format(option, command, c_option)
   
def get_docker_pull(option='', image_name=''):
    return '''
docker pull {0} {1} 
    '''.format(option, image_name)
    
def get_decker_run(option='', image='', command='', arg=''):
    return '''
docker run {0} {1} {2} {3}
    '''.format(option, image, command, arg)