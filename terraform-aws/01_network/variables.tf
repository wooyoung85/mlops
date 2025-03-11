variable "region" {
  description = "AWS Region"
  default     = "ap-northeast-2"
}
 
variable "vpc_cidr" {
  description = "VPC CIDR block"
  default     = "10.0.0.0/20"
}
 
variable "public_subnet_cidr" {
  description = "Public Subnet CIDR block"
  default     = "10.0.1.0/24"
}

variable "elastic_ip" {
  description = "Elastic IP address for the instance"
  default     = ""
}