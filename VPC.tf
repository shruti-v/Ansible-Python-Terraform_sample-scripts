provider "aws" {
  region = "us-east-1"
}

##########VPC###################
resource "aws_vpc" "VPC_NEW" {
  cidr_block = "10.0.0.0/16"
}

############Internet gateway###############

resource "aws_internet_gateway" "Gateway" {
  vpc_id = aws_vpc.VPC_NEW.id

  tags = {
    Name = "GW"
  }
}

###########subnet####################

resource "aws_subnet" "Subnet1" {
  vpc_id     = aws_vpc.VPC_NEW.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "Subnet1"
  }
}

resource "aws_subnet" "Subnet2" {
  vpc_id     = aws_vpc.VPC_NEW.id
  cidr_block = "10.0.2.0/24"

  tags = {
    Name = "Subnet2"
  }
}

#####################Route table###################

resource "aws_route_table" "RT" {
  vpc_id = aws_vpc.VPC_NEW.id

  route = []
  tags = {
    Name = "RT"
  }
}

########################### Route ########################

resource "aws_route" "R" {
  route_table_id         = aws_route_table.RT.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.Gateway.id

}

