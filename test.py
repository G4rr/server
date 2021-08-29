import blockstf.btf as btf
import blockstf.udtf as udtf
import blockstf.bcdktf as bcdktf

import os

access_key=""
secret_key=""

def build_infrastructure_tf(filename="aws-infrastructure/setup.tf"):
    with open(filename, 'w') as aws_tf: 
        aws_tf.write(btf.get_provider(region="eu-central-1"))
        aws_tf.write(btf.get_aws_ami())
        aws_tf.write(btf.get_aws_security_group())
        aws_tf.write(btf.get_aws_launch_configuration())
        print("Terraform file has been created")
 
def build_infrastructure_sh(filename="aws-infrastructure/setup.sh"):
    with open(filename, 'w') as aws_sh:
        aws_sh.write(udtf.get_default_introduction())
        print("User data file has been created")

def build_aws_infrastructure():
    export_access_key='export AWS_ACCESS_KEY_ID='+access_key
    export_secret_key='export AWS_SECRET_ACCESS_KEY='+secret_key
    os.system(export_access_key)
    os.system(export_secret_key)
    os.system('cd aws-infrastructure')
    os.system('terraform init')
    os.system('terraform apply -auto-approve')
    
    print("Successful")
        
if __name__ == "__main__":
    build_infrastructure_tf()
    build_infrastructure_sh()
    build_aws_infrastructure()    
