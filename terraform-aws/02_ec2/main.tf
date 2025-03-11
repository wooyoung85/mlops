provider "aws" {
  region = "ap-northeast-2"
}

data "terraform_remote_state" "network" {
  backend = "local"  # 이 예에서는 로컬 백엔드를 사용
  config = {
    path = "../01_network/terraform.tfstate"  # 네트워크 상태 파일의 경로
  }
}

# EC2 인스턴스 생성
resource "aws_instance" "kf_instance" {
  count                     = 1
  ami                       = var.ami_id
  instance_type             = var.kf_instance_type
  subnet_id                 = data.terraform_remote_state.network.outputs.public_subnet_id
  vpc_security_group_ids    = [data.terraform_remote_state.network.outputs.security_group_id]

  associate_public_ip_address = false  # 퍼블릭 IP 자동 할당 비활성화
  key_name                   = var.key_name

  # EBS 볼륨 설정
  root_block_device {
    volume_size = 500  # 500GB
    volume_type = "gp3"  # 일반적인 SSD 타입
  }

  tags = {
    Name = "kf-instance-${count.index + 1}"
  }
}

# Elastic IP와 EC2 인스턴스 연결
resource "aws_eip_association" "kf_eip_association" {
  instance_id  = aws_instance.kf_instance[0].id  # 첫 번째 인스턴스에 연결
  allocation_id = data.terraform_remote_state.network.outputs.eip_allocation_id  # Elastic IP 할당 ID
}

# 출력
output "instance_ips" {
  value = {
    for instance in aws_instance.kf_instance :
    instance.tags["Name"] => {
      public_ip  = data.terraform_remote_state.network.outputs.elastic_ip,  # Elastic IP 사용
      private_ip = instance.private_ip
    }
  }
}