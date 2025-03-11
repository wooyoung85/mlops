# AWS CLI Install
```bash
sudo apt-get install -y unzip
cd
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

aws --version
aws configure

AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: ap-northeast-2
Default output format [None]: json
```


# Terraform Install
```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt-get update -y

sudo apt-get install -y terraform

terraform -install-autocomplete
source ~/.bashrc

cd ~/dev/mlops/terraform-aws/01_network
cd ~/dev/mlops/terraform-aws/02_ec2

terraform init
terraform plan
terraform apply -auto-approve
terraform refresh
terraform destroy -auto-approve
```

# Terraform 환경변수 설정
```bash
# Red Hat의 AWS 계정 ID로 이미지 검색
aws ec2 describe-images --owners 309956199498 --filters "Name=name,Values=*RHEL-8.6*" --query "Images[*].[ImageId, Name]" --output table
```

# 접속
```bash
$> chmod 400 ~/wyseo.pem
$> ll ~/wyseo.pem
-r-------- 1 wooyoung wooyoung 1.7K Feb  6 16:36 /home/wooyoung/wyseo.pem

# rm -rf ~/.ssh
PUBLIC_IP=3.36.163.33
ssh -i ~/wyseo.pem ec2-user@$PUBLIC_IP
```