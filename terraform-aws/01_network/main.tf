provider "aws" {
  region = var.region
}

# VPC 생성
resource "aws_vpc" "kf_vpc" {
  cidr_block = var.vpc_cidr

  tags = {
    Name = "kf-vpc"
  }
}

# 퍼블릭 서브넷 생성
resource "aws_subnet" "kf_public_subnet" {
  vpc_id            = aws_vpc.kf_vpc.id
  cidr_block        = var.public_subnet_cidr
  availability_zone = "ap-northeast-2a"

  tags = {
    Name = "kf-public-subnet"
  }
}

# 인터넷 게이트웨이 생성
resource "aws_internet_gateway" "kf_igw" {
  vpc_id = aws_vpc.kf_vpc.id

  tags = {
    Name = "kf-internet-gateway"
  }
}

# 퍼블릭 서브넷에 대한 라우트 테이블 생성
resource "aws_route_table" "kf_public_route_table" {
  vpc_id = aws_vpc.kf_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.kf_igw.id
  }

  tags = {
    Name = "kf-public-route-table"
  }
}

# 퍼블릭 서브넷에 라우트 테이블 연결
resource "aws_route_table_association" "kf_public_route_table_association" {
  subnet_id      = aws_subnet.kf_public_subnet.id
  route_table_id = aws_route_table.kf_public_route_table.id
}

# EC2 인스턴스에 대한 보안 그룹
resource "aws_security_group" "kf_sg" {
  vpc_id = aws_vpc.kf_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # 모든 IP에서 SSH 접근 허용
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"  # 모든 아웃바운드 트래픽 허용
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "kf-sg"
  }
}

resource "aws_eip" "kf_eip" {
}

output "public_subnet_id" {
  value = aws_subnet.kf_public_subnet.id
}

output "security_group_id" {
  value = aws_security_group.kf_sg.id
}

output "eip_allocation_id" {
  value = aws_eip.kf_eip.id  # Elastic IP의 할당 ID 출력
}

output "elastic_ip" {
  value = aws_eip.kf_eip.public_ip  # 생성된 Elastic IP 출력
}