```bash
# Terraform 사용을 위한 별도 인증 필요
gcloud auth application-default login

# Project ID 조회
gcloud config get-value project

# Quota 수정
## https://console.cloud.google.com/iam-admin/quotas
│ Error: Error waiting for instance to create: Quota 'CPUS' exceeded.  Limit: 24.0 in region asia-northeast3.
│       metric name = compute.googleapis.com/cpus
│       limit name = CPUS-per-project-region
│       limit = 24
│       dimensions = map[region:asia-northeast3]

│ Error: Error waiting for instance to create: Quota 'CPUS_ALL_REGIONS' exceeded.  Limit: 12.0 globally.
│       metric name = compute.googleapis.com/cpus_all_regions
│       limit name = CPUS-ALL-REGIONS-per-project
│       limit = 12
│       dimensions = map[global:global]

# Terraform CLI
cd ~/dev/mlops/terraform-gcp/01_network
cd ~/dev/mlops/terraform-gcp/02_instance

terraform init
terraform plan
terraform apply -auto-approve
terraform refresh
terraform destroy -auto-approve
```