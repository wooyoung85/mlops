

# Python install
```bash
yum update -y --exclude=kubelet,kubeadm,kubectl
 
sudo dnf install yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel -y
sudo dnf install sqlite-devel -y

cd /opt
PYTHON_VERSION=3.10
PYTHON_VERSION_DETAIL=3.10.9
  
sudo curl -LO https://www.python.org/ftp/python/$PYTHON_VERSION_DETAIL/Python-$PYTHON_VERSION_DETAIL.tgz
sudo tar xzf Python-$PYTHON_VERSION_DETAIL.tgz
cd Python-$PYTHON_VERSION_DETAIL

sudo ./configure --enable-optimizations
sudo make altinstall
 
sudo ln -fs /usr/local/bin/python$PYTHON_VERSION /usr/bin/python
python -V

sudo ln -fs /usr/local/bin/pip$PYTHON_VERSION /usr/bin/pip
pip -V

sqlite3 --version
```

# Airflow Install

```bash
export AIRFLOW_HOME=~/airflow
mkdir -p $AIRFLOW_HOME/logs
cd $AIRFLOW_HOME

AIRFLOW_VERSION=2.10.4
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

curl -L "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt" -o ~/constraints-${PYTHON_VERSION}.txt

# Airflow Install
python -m venv airflow_venv && source airflow_venv/bin/activate 
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "constraints-${PYTHON_VERSION}.txt"

# Airflow DB 초기화
airflow db migrate

# Airflow Admin 계정 생성 (Password는 직접 입력)
airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@airflow.com

# Logging 설정
cat << EOF > $AIRFLOW_HOME/logging_config.py
import os
from logging.handlers import TimedRotatingFileHandler

AIRFLOW_HOME = os.getenv("AIRFLOW_HOME", "~/airflow")
LOG_DIR = os.path.expanduser(f"{AIRFLOW_HOME}/logs")

LOG_FORMAT = "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "airflow_default": {
            "format": LOG_FORMAT,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "airflow_default",
        },
        "webserver": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "airflow_default",
            "filename": f"{LOG_DIR}/webserver.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
        },
        "scheduler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "airflow_default",
            "filename": f"{LOG_DIR}/scheduler.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
        },
    },
    "loggers": {
        "airflow.webserver": {
            "handlers": ["webserver"],
            "level": "INFO",
            "propagate": False,
        },
        "airflow.scheduler": {
            "handlers": ["scheduler"],
            "level": "INFO",
            "propagate": False,
        },
        "airflow.task": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
EOF

# airflow.cfg에 로깅 설정 적용
sed -i 's/# logging_config_class =/logging_config_class = logging_config.LOGGING_CONFIG/' $AIRFLOW_HOME/airflow.cfg

# Airflow 웹서버 실행 (포트 8080)
pkill -f "airflow webserver"
nohup airflow webserver --port 8080 > /dev/null 2>&1 &

# Airflow 스케줄러 실행
pkill -f "airflow scheduler"
nohup airflow scheduler > /dev/null 2>&1 &
```