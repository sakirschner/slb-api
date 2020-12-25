variable "prefix" {
  default = "raad"
}

variable "project" {
  default = "student-leader-board-api"
}

variable "contact" {
  default = "scottadev@gmail.com"
}

variable "db_username" {
  description = "Username for the RDS postgres instance"
}

variable "db_password" {
  description = "Password for the RDS postgres instance"
}

variable "bastion_key_name" {
  default = "student-leader-board-api-bastion"
}

variable "ecr_image_api" {
  description = "ECR image for API"
  default     = "964127226690.dkr.ecr.us-east-1.amazonaws.com/student-leader-board-api-devops:latest"
}

variable "ecr_image_proxy" {
  description = "ECR image for proxy"
  default     = "964127226690.dkr.ecr.us-east-1.amazonaws.com/student-leader-board-api-proxy"
}

variable "django_secret_key" {
  description = "Secret key for Django app"
}

variable "dns_zone_name" {
  description = "Domain Name"
  default     = "scottakdev.com"
}

variable "subdomain" {
  description = "Subdomain per environment"
  type        = map(string)
  default = {
    production = "api"
    staging    = "api.staging"
    dev        = "api.dev"
  }
}