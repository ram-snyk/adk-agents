terraform {
  required_version = ">= 1.0"
  
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Variables
variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

# Cloud Run service for ADK agent
resource "google_cloud_run_service" "adk_agent" {
  name     = "adk-agent-${var.environment}"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/adk-agent:latest"
        
        resources {
          limits = {
            cpu    = "1000m"
            memory = "512Mi"
          }
        }
        
        env {
          name = "GOOGLE_API_KEY"
          value_from {
            secret_key_ref {
              name = google_secret_manager_secret.api_key.secret_id
              key  = "latest"
            }
          }
        }

        ports {
          container_port = 8080
        }
      }
      
      service_account_name = google_service_account.adk_agent.email
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "10"
        "autoscaling.knative.dev/minScale" = "1"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Service account for Cloud Run
resource "google_service_account" "adk_agent" {
  account_id   = "adk-agent-${var.environment}"
  display_name = "ADK Agent Service Account"
  description  = "Service account for ADK agent Cloud Run service"
}

# Secret Manager for API key
resource "google_secret_manager_secret" "api_key" {
  secret_id = "google-api-key-${var.environment}"

  replication {
    automatic = true
  }
}

# IAM binding for service account to access secret
resource "google_secret_manager_secret_iam_binding" "api_key_access" {
  secret_id = google_secret_manager_secret.api_key.id
  role      = "roles/secretmanager.secretAccessor"
  members = [
    "serviceAccount:${google_service_account.adk_agent.email}"
  ]
}

# Cloud Storage bucket for logs and artifacts
resource "google_storage_bucket" "adk_logs" {
  name          = "${var.project_id}-adk-logs-${var.environment}"
  location      = var.region
  force_destroy = false

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  # Enable logging for audit trail
  logging {
    log_bucket = google_storage_bucket.adk_audit_logs.name
  }

  # Use customer-managed encryption key
  encryption {
    default_kms_key_name = google_kms_crypto_key.bucket_key.id
  }

  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "Delete"
    }
  }
}

# Separate bucket for audit logs
resource "google_storage_bucket" "adk_audit_logs" {
  name          = "${var.project_id}-adk-audit-logs-${var.environment}"
  location      = var.region
  force_destroy = false

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  # Use customer-managed encryption key
  encryption {
    default_kms_key_name = google_kms_crypto_key.bucket_key.id
  }

  lifecycle_rule {
    condition {
      age = 365
    }
    action {
      type = "Delete"
    }
  }
}

# KMS keyring for encryption
resource "google_kms_key_ring" "adk_keyring" {
  name     = "adk-keyring-${var.environment}"
  location = var.region
}

# KMS crypto key for bucket encryption
resource "google_kms_crypto_key" "bucket_key" {
  name     = "adk-bucket-key"
  key_ring = google_kms_key_ring.adk_keyring.id

  rotation_period = "7776000s" # 90 days

  lifecycle {
    prevent_destroy = true
  }
}

# IAM binding for Cloud Storage to use KMS key
resource "google_kms_crypto_key_iam_binding" "storage_key_binding" {
  crypto_key_id = google_kms_crypto_key.bucket_key.id
  role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"

  members = [
    "serviceAccount:service-${data.google_project.project.number}@gs-project-accounts.iam.gserviceaccount.com"
  ]
}

# Data source to get project number
data "google_project" "project" {
  project_id = var.project_id
}

# IAM policy for Cloud Run (public access for demo - should be restricted in production)
resource "google_cloud_run_service_iam_binding" "public_access" {
  service  = google_cloud_run_service.adk_agent.name
  location = google_cloud_run_service.adk_agent.location
  role     = "roles/run.invoker"
  members = [
    "allUsers"
  ]
}

# Outputs
output "service_url" {
  description = "URL of the deployed Cloud Run service"
  value       = google_cloud_run_service.adk_agent.status[0].url
}

output "service_account_email" {
  description = "Email of the service account"
  value       = google_service_account.adk_agent.email
}
