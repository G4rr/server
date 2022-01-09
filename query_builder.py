import blockstf.btf as btf
import blockstf.udtf as udtf

#
def build_iac_tf(instance, filename="aws-iac/setup.tf"):
    with open(filename, 'w') as aws_tf:
        aws_tf.write(btf.get_provider(region=instance.get_region()))
        aws_tf.write(btf.get_aws_key_pair(public_key=instance.get_keys().get_public_key()))
        aws_tf.write(btf.get_aws_instance())
        aws_tf.write(btf.get_aws_all_sg())
        print("Terraform file has been created")

#
def build_iac_sh(filename="aws-iac/setup.sh"):
    with open(filename, 'w') as aws_sh:
        aws_sh.write(udtf.get_default_introduction())
        print("User data file has been created")

#
def build_iac():
    os.chdir('aws-iac')
    print(export_access_key)
    print(export_secret_key)
    os.system('%s',"export AWS_ACCESS_KEY_ID="+export_access_key)
    os.system('%s',"export AWS_SECRET_ACCESS_KEY="+export_secret_key)
    os.system('terraform init')
    os.system('terraform apply -auto-approve')
    print("Successful")
    os.chdir('../')

#
def destroy_aws_iac():
    os.chdir('aws-iac')
    os.system('terraform destroy')
    os.chdir('../')
#
def scan_request(application_scan_name, url, bool_scanners):
    print('Name:', application_scan_name)
    print('URL:', url)
    print('bool_owasp:', bool_scanners[0])
    print('bool_nikto:', bool_scanners[1])
    print('bool_wapiti:', bool_scanners[2])

    #if (bool_owasp):
    #    aws_sh.write(udtf.get_docker_run(image_name='owasp/zap2docker-stable'))
    #if (bool_nikto):
    #    aws_sh.write(udtf.get_docker_run(image_name='frapsoft/nikto'))
    #if (bool_w3af):
    #    aws_sh.write(udtf.get_docker_run(image_name='andresriancho/w3af'))
    #if (bool_wapiti):
    #    aws_sh.write(udtf.get_docker_run(image_name='sammascanner/wapiti'))

#
def build_report():
    print("build_report")



#
def setup():
    build_iac()
