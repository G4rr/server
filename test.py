import blockstf.btf as btf
import blockstf.udtf as udtf
import blockstf.bcdktf as bcdktf

import os

access_key=""
secret_key=""

def build_iac_tf(filename="aws-iac/setup.tf"):
    with open(filename, 'w') as aws_tf: 
        aws_tf.write(btf.get_provider(region="eu-central-1"))
        #aws_tf.write(btf.get_aws_ami())
        aws_tf.write(btf.get_aws_instace())
        aws_tf.write(btf.get_aws_security_group())
        
        print("Terraform file has been created")
 
def build_iac_sh(filename="aws-iac/setup.sh"):
    with open(filename, 'w') as aws_sh:
        aws_sh.write(udtf.get_default_introduction())
        print("User data file has been created")

def build_aws_iac():
    export_access_key='export AWS_ACCESS_KEY_ID='+access_key
    export_secret_key='export AWS_SECRET_ACCESS_KEY='+secret_key
    os.system(export_access_key)
    os.system(export_secret_key)
    os.system('cd aws-iac')
    os.system('terraform init')
    os.system('terraform apply -auto-approve')
    
    print("Successful")
        
if __name__ == "__main__":
    build_iac_tf()
    build_iac_sh()
    build_aws_iac()    
