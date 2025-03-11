provider "google" {
  project = var.project_id
  region  = var.region
}

# Static IP 주소 생성
resource "google_compute_address" "kubeflow_static_ip" {
  name   = "kubeflow-static-ip"
  region = var.region
}

# 방화벽 규칙 설정
resource "google_compute_firewall" "allow_http_port" {
  name    = "allow-http-port"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  target_tags   = ["http-server"]
  source_ranges = ["0.0.0.0/0"]
  direction     = "INGRESS"
  priority      = 1000
}

resource "google_compute_firewall" "allow_https_port" {
  name    = "allow-https-port"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["443"]
  }

  target_tags   = ["https-server"]
  source_ranges = ["0.0.0.0/0"]
  direction     = "INGRESS"
  priority      = 1000
}

resource "google_compute_firewall" "allow_k8s_nodeport" {
  name    = "allow-k8s-nodeport"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["30000-32767"]
  }

  target_tags   = ["k8s"]
  source_ranges = ["0.0.0.0/0"]
  direction     = "INGRESS"
  priority      = 1000
}