
# gcloud CLI 설치

```bash
sudo apt-get update -y

sudo apt-get install -y apt-transport-https ca-certificates gnupg curl
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

sudo apt-get -y update && sudo apt-get install -y google-cloud-cli

```

# 인스턴스 생성
```bash
# Google Cloud 설정
gcloud init
 
PROJECT=$(gcloud config get-value project)
ACCOUNT=$(gcloud config get-value account)
ZONE=$(gcloud config get-value compute/zone)
# ZONE=us-central1-a
echo $PROJECT
echo $ACCOUNT
echo $ZONE
 
gcloud compute addresses create kubeflow-static-ip \
    --region asia-northeast3 \
    --description "Kubeflow static public IP address"
 
KUBEFLOW_IP=$(gcloud compute addresses list --regions asia-northeast3 --format="value(address)")
echo $KUBEFLOW_IP
 
# Kubeflow 인스턴스 생성
# gcloud compute instances delete kubeflow
gcloud compute instances create kubeflow \
    --project=$PROJECT \
    --zone=$ZONE \
    --machine-type=e2-standard-4 \
    --image-family=rhel-8 \
    --image-project=rhel-cloud \
    --boot-disk-size=500GB \
    --tags=http-server,https-server,k8s \
    --metadata=startup-script="yum update -y" \
    --address=$KUBEFLOW_IP
 
gcloud compute instances create kubeflow-w1 \
    --project=$PROJECT \
    --zone=$ZONE \
    --machine-type=e2-standard-16 \
    --image-family=rhel-8 \
    --image-project=rhel-cloud \
    --boot-disk-size=200GB \
    --tags=http-server,https-server,k8s \
    --metadata=startup-script="yum update -y"

# Nodeport 방화벽 Open
gcloud compute firewall-rules create allow-k8s-nodeport \
    --allow tcp:30000-32767 \
    --target-tags k8s \
    --description "Allow traffic on ports 30000 to 32767 for K8S" \
    --direction INGRESS \
    --priority 1000
 
gcloud compute instances add-tags kubeflow --tags http-server,https-server,k8s --zone $ZONE
 
 
# SSH 설정
gcloud compute config-ssh --ssh-key-file=~/.ssh/gcp_rsa
ssh kubeflow.$ZONE.$PROJECT

gcloud compute config-ssh --ssh-key-file=~/.ssh/gcp_rsa
ssh kubeflow-w1.$ZONE.$PROJECT
```