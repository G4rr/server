
provider "aws" { 
  region = "eu-central-1"
}
data "aws_availability_zones" "available" {}
    
data "aws_ami" "latest_linux" {
  owners      = ["099720109477"]
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}
    
resource "aws_security_group" "web_sg" {
  name_prefix        = "Web_SG-"
  description = "Dynamic SecurityGroup for WebServers"
  
  dynamic "ingress" {
    for_each = ["22", "80", "443", "8080"]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name  = "Dynamic SecurityGroup"
    Owner = "Oleksii Pryshchepa"
  }
    
resource "aws_launch_configuration" "prod_instnc" {
  name_prefix     = "WebServer-"
  image_id        = data.aws_ami.latest_linux.id
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.web_sg.id]

  user_data = file("pentool-setup.sh")

  lifecycle {
    create_before_destroy = true
  }
}
    