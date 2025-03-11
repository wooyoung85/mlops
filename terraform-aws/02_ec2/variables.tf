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
 
variable "kf_instance_type" {
  description = "Kubeflow instance type"
  default     = "g4dn.8xlarge"
}
 
variable "ami_id" {
  description = "AMI ID for the instances"
  default     = "ami-0d9478bea993499d8"
}
 
variable "key_name" {
  description = "Key pair name for EC2 instances"
  default     = "wyseo"
}

variable "elastic_ip" {
  description = "Kubeflow instance Public IP"
  default     = "3.37.7.81"
}