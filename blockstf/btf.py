# Blocks of Terraform modules
def get_provider(provider='aws', region='eu-central-1'):
    return '''provider "%s" {
  region = "%s"
}'''%(provider, region)


def get_aws_availability_zones():
    return '''
data "aws_availability_zones" "available" {}
    '''

def get_aws_key_pair(public_key):
    return '''
resource "aws_key_pair" "pub_key" {
  key_name   = "SSH-key"
  public_key = "%s"
}
    '''%(public_key)

def get_aws_ami(owners='099720109477', name='name', value='ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*'):
    return '''
data "aws_ami" "latest_linux" {
  owners      = ["%s"]
  most_recent = true
  filter {
    name   = "%s"
    values = ["%s"]
  }
}
    '''%(owners, name, value)

def get_aws_eip(tag_name="TEST_EIP", tag_owner="Oleksii Pryshchepa"):
    return '''
resource "aws_eip" "instance_eip" {
  instance = aws_instance.my_webserver.id
  }
  tags = {
    Name  = "%s"
    Owner = "%s"
  }
}
    '''%(tag_name, tag_owner)

def get_aws_instance(ami='ami-05f7491af5eef733a', itype='t3.micro', tag_name="TEST_INSTANCE", tag_owner="Oleksii Pryshchepa"):
    return '''
resource "aws_instance" "webserver" {
  ami                    = "%s"
  instance_type          = "%s"
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  user_data              = file("setup.sh")

  lifecycle {
    create_before_destroy = true
  }
  tags = {
    Name  = "%s"
    Owner = "%s"
  }
}
    '''%(ami, itype, tag_name, tag_owner)

def get_aws_sg():
    return '''
resource "aws_security_group_rule" "web_sg" {
  type              = "ingress"
  from_port         = 0
  to_port           = 65535
  protocol          = "tcp"
  security_group_id = "sg-123456"
}
'''

def get_aws_all_sg(tag_name="TEST_DSG", tag_owner="Oleksii Pryshchepa"):
    return '''
resource "aws_security_group" "web_sg" {
  name_prefix        = "Web_SG-"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name  = "%s"
    Owner = "%s"
  }
 }
    '''%(tag_name, tag_owner)

def get_aws_launch_configuration(instance_type='t2.micro'):
    return '''
resource "aws_launch_configuration" "prod_instnc" {
  name_prefix     = "WebServer-"
  image_id        = data.aws_ami.latest_linux.id
  instance_type   = "%s"
  security_groups = [aws_security_group.web_sg.id]

  user_data = file("setup.sh")

  lifecycle {
    create_before_destroy = true
  }
}
    '''%(instance_type)

def get_aws_autoscaling_group():
    return '''
resource "aws_autoscaling_group" "prod_instnc" {
  name                 = "ASG-${aws_launch_configuration.prod_instnc.name}"
  launch_configuration = aws_launch_configuration.prod_instnc.name
  min_size             = 2
  max_size             = 3
  min_elb_capacity     = 2
  health_check_type    = "ELB"
  vpc_zone_identifier  = [aws_default_subnet.default_az1.id, aws_default_subnet.default_az2.id]
  load_balancers       = [aws_elb.prod_instnc.name]

  dynamic "tag" {
    for_each = {
      Name  = "WebServer in ASG"
      Owner = "Oleksii Pryshchepa"
    }
    content {
      key                 = tag.key
      value               = tag.value
      propagate_at_launch = true
    }
  }

  lifecycle {
    create_before_destroy = true
  }
}
    '''

def get_aws_elb():
    return '''
resource "aws_elb" "prod_instnc" {
  name               = "WebServer-on-ELB"
  availability_zones = [data.aws_availability_zones.available.names[0], data.aws_availability_zones.available.names[1]]
  security_groups    = [aws_security_group.web_sg.id]
  listener {
    lb_port           = 80
    lb_protocol       = "http"
    instance_port     = 80
    instance_protocol = "http"
  }
  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 3
    target              = "HTTP:80/"
    interval            = 10
  }
  tags = {
    Name = "WebServer-ELB"
  }
}
    '''

def get_aws_default_subnet():
    return '''
resource "aws_default_subnet" "default_az1" {
  availability_zone = data.aws_availability_zones.available.names[0]
}
    '''

def get_local_file():
    return '''
resource "local_file" "dns" {
  content  = aws_elb.prod_instnc.dns_name
  filename = "../dns.txt"
}
    '''
