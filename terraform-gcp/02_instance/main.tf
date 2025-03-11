provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

# Compute Instance 생성
resource "google_compute_instance" "kubeflow" {
  name         = "kubeflow"
  machine_type = "e2-standard-16"
  zone         = var.zone
  tags         = ["http-server", "https-server", "k8s"]

  boot_disk {
    initialize_params {
      image = "rhel-cloud/rhel-8"
      size  = 500 # in GB
    }
  }

  network_interface {
    network = "default"
    access_config {
      nat_ip = data.google_compute_address.kubeflow_static_ip.address
    }
  }

  metadata_startup_script = "yum update -y"
}

# Data source to fetch the static IP from the network module
data "google_compute_address" "kubeflow_static_ip" {
  name   = "kubeflow-static-ip"
  region = var.region
}

output "ssh_command" {
  value = "gcloud compute config-ssh --ssh-key-file=~/.ssh/gcp_rsa\nssh ${google_compute_instance.kubeflow.name}.${var.zone}.${var.project_id}"
  description = "The SSH command to connect to the Kubeflow instance"
}