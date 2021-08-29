# Blocks of cdktf
def get_cdktf_default_libreries():
    return '''
    from constructs import Construct
    from cdktf import App, TerraformStack, TerraformOutput
    from imports.aws import AwsProvider, Instance '''

def get_cdktf_class():
    return '''
    class MyStack(TerraformStack):
        def __init__(self, scope: Construct, ns: str):
            super().__init__(scope, ns)
    '''

def get_cdktf_aws_region(provider='Aws', region='us-east-1'):
    return '''
        AwsProvider(self, {0}, region='{1}') 
    '''.format(provider, region)

def get_cdktf_aws_instance(name="Test", ami="ami-01456a894f71116f2", ec2_type="t2.micro"):
    return '''
        ec2 = Instance(self, {0},
          ami={1},
          instance_type={2},
        ) 
    '''.format(name, ami,ec2_type)

def get_cdktf_output(output_name='hello_public_ip', value='public_ip'):
    return '''
        TerraformOutput(self, {0},
          value=ec2.{1}
        )
    '''.format(output_name, value)
        
def get_cdktf_app(app_name='hello-terraform'):
    return '''
    app = App()
    MyStack(app, {0})
    app.synth()
    '''.format(app_name)

