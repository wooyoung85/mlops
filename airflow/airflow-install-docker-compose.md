# Docker 설치
```bash
# sudo su -
# yum update -y

# Set up the repository
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

# Install Docker Engine
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


mkdir -p /root/files/rpm
cd /root/files/rpm

dnf download --resolve --destdir=/root/files/rpm dnf-plugins-core

dnf download --resolve --destdir=/root/files/rpm docker-ce
dnf download --resolve --destdir=/root/files/rpm docker-ce-cli

dnf download --resolve --destdir=/root/files/rpm containerd.io
dnf download --resolve --destdir=/root/files/rpm docker-buildx-plugin
dnf download --resolve --destdir=/root/files/rpm docker-compose-plugin

dnf localinstall -y /root/files/rpm/*.rpm



sudo systemctl enable --now docker

# Manage Docker as a non-root user
sudo groupadd docker
sudo usermod -aG docker $USER
docker ps

# Configure Docker to start on boot with systemd
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```


# Airflow 설치
```bash
# Memory Check (8GB 이상)
numfmt --to=iec $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE)))

# Setting the right Airflow user
mkdir ~/airflow && cd ~/airflow
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

# echo "AIRFLOW_UID=50000" > .env


cd ~/airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.4/docker-compose.yaml'


docker compose up airflow-init



docker compose up -d


docker compose run airflow-worker airflow info

```

# Aireflow Plugin
```bash
vim ~/airflow/docker-compose.yaml
###################################
x-airflow-common:
  &airflow-common
  # In order to add custom dependencies or upgrade provider packages you can use your extended image.
  # Comment the image line, place your Dockerfile in the directory where you placed the docker-compose.yaml
  # and uncomment the "build" line below, Then run `docker-compose build` to build the images.
  image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.10.4}
  build: .
  environment:
    &airflow-common-env
    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
    AIRFLOW__CODE_EDITOR__ROOT_DIRECTORY: /opt/airflow/dags
    AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL: 10    

###################################


vim ~/airflow/Dockerfile
###################################
FROM apache/airflow:2.10.4
RUN pip install apache-airflow-providers-standard
RUN pip install airflow-code-editor
RUN pip install black isort fs-s3fs fs-gcsfs
###################################

cd ~/airflow
docker compose build
docker compose up -d

docker logs airflow-airflow-webserver-1 -f


docker exec -it airflow-airflow-webserver-1 /bin/bash
docker exec -it airflow-airflow-worker-1 /bin/bash
```