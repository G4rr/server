import blokstf.btf as btf

print(btf.get_default_libreries())
print(btf.get_class())
print(btf.get_aws_region(region="us-west-1"))
print(btf.get_aws_instance(name="PenTool", ec2_type="t3.small"))
print(btf.get_tf_output())
print(btf.get_app("PenTool_App"))
