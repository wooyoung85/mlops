# Enterprise MLOps

## Prerequisite (실습환경 준비)

- 최소 요구 Spec : `CPU - 16 Core, MEM - 32 GB, DISK - 100 GB` 
- 권장 요구 Spec : `CPU - 32 Core, MEM - 64 GB, DISK - 200 GB` 
- OS : `RHEL8`, `ROCKY8` (Kernel 4.X)
- Kubeflow/Keycloak/MinIO에 적용할 Domain 
   - https://kubeflow.example.com
   - https://keycloak.example.com
   - http://minio.example.com

### AWS

[Terraform - AWS EC2 Create](./terraform-aws/install.md)

### GCP

[Terraform - GCP Compute Engine Create](./terraform-gcp/install.md)  
✅[gcloud cli - GCP Compute Engine Create](./gcp/instance-create-kubeflow.md)

## 목차

### 1. Kubernetes Cluster Install
   1. [Kubernetes Node GPU Driver Install](./kubeflow-single-node/1-1.online-gpu-driver.md)
   2. ✅[Kubernetes Node Pre Install](./kubeflow-single-node/1-2.online-pre-install.md)
   3. [Kubernetes Install File Download (Offline)](./kubeflow-single-node/1-3.offline-download-install-file.md)
   4. [Kubernetes Node Pre Install (Offline)](./kubeflow-single-node/1-4.offline-pre-install.md)
   5. ✅[Kubernetes Install](./kubeflow-single-node/1-5.k8s-install.md)
   6. [Nvidia Device Plugin Install](./kubeflow-single-node/1-6.nvidia-device-plugin.md)
   7. [Kind Cluster](./kubeflow-single-node/1-7.kind.md)

### 2. Kubeflow Install
   1. ✅[Kubeflow Install (v.1.9.1)](./kubeflow-single-node/2-1.kubeflow-install.md)
   2. ✅[Kubeflow Expose (HAProxy, Nginx Ingress Controller)](./kubeflow-single-node/2-2.kubeflow-expose.md)
   3. ✅[Nginx Ingress Controller TLS Config](./kubeflow-single-node/2-3.ssl-config.md)

### 3. Supporting System Install 
   1. ✅[Keycloak Install](./kubeflow-single-node/3-1.keycloak-helm.md)
   2. ✅[Integration Keycloak and Dex](./kubeflow-single-node/3-2.keycloak-dex.md)
   3. ✅[MinIO Install](./kubeflow-single-node/3-3.minio.md)
   4. [Harbor Install](./kubeflow-single-node/3-4.harbor.md)
   5. ✅[Prometheus Stack Install](./kubeflow-single-node/3-5.monitoring.md)
   6. [Loki Stack Install](./kubeflow-single-node/3-6.logging.md)
   7. [Airflow Install](./kubeflow-single-node/3-7.airflow-install-pip.md)

### 4. Custom Notebook Image
   1. [Custom Notebook Image Build](./kubeflow-single-node/4-1.custom-image-build.md)
   2. [Custom Notebook Image Build (KB)](./kubeflow-single-node/4-2.custom-image-kb.md)
   3. [Custom Notebook Image Build with Dockerfile](./kubeflow-single-node/4-3.custom-image-dockerfile.md)

### 5. Notebook Stress Test
   1. [Notebook Stress Test Summary](./kubeflow-single-node/5-1.stress-test-summary.md)
   2. [CPU Stress Test](./kubeflow-single-node/5-2.cpu-test-result.md)
   3. [Mem Stress Test](./kubeflow-single-node/5-3.memory-test-result.md)
   4. [Disk Stress Test](./kubeflow-single-node/5-4.disk-test-result%20copy.md)
   5. [GPU Perform Test](./kubeflow-single-node/5-5.gpu-test.md)

### 6. Model Registry
   1. [Model Registry Install](./kubeflow-single-node/6-1.model-registry.1md)
   2. [Model Registry UI Install](./kubeflow-single-node/6-2.model-registry-ui.md)   
   3. [~~MLFlo Install~~](./kubeflow-single-node/6-3.mlflow.md)

### 7. KServe
   1. [KServe Model Serving - PVC](./kubeflow-single-node/7-1.kserve-pvc.md)
   2. [KServe Model Serving - S3](./kubeflow-single-node/7-2.kserve-s3.md)
   3. [KServe Model External Expose](./kubeflow-single-node/7-3.kserve-external-expose.md)

### 8. Katib
   1. [Katib Guide](./kubeflow-single-node/8-1.katib-guide.md)

### 9. Pipeline
   1. [Pipeline Guide](./kubeflow-single-node/9-1.pipeline-guide.md)

### 10. Manifest
   1. [Notebook Manifest](./kubeflow-single-node/4-1.notebook.md)
   2. [Profile Manifest](./kubeflow-single-node/10-2.profile.md)
   3. [User Manifest](./kubeflow-single-node/10-3.user.md)

### 11. Admin
   1. [Notebook IDLE Time Config](./kubeflow-single-node/11-1.notebook-idle-time-config.md)
---
