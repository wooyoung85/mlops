
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
echo $PROJECT
echo $ACCOUNT
echo $ZONE

gcloud compute firewall-rules create allow-airflow-port \
    --direction=INGRESS \
    --priority=1000 \
    --network=default \
    --action=ALLOW \
    --rules=tcp:8080 \
    --source-ranges=0.0.0.0/0 \
    --target-tags=airflow

 
# airflow 인스턴스 생성
# gcloud compute instances delete airflow
gcloud compute instances create airflow \
    --project=$PROJECT \
    --zone=$ZONE \
    --machine-type=e2-standard-8 \
    --image-family=rhel-8 \
    --image-project=rhel-cloud \
    --boot-disk-size=100GB \
    --tags=http-server,https-server,airflow \
    --metadata=startup-script="yum update -y"
 
 
# SSH 설정
gcloud compute config-ssh --ssh-key-file=~/.ssh/gcp_rsa
ssh airflow.$ZONE.$PROJECT
```