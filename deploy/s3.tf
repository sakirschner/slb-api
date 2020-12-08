resource "aws_s3_bucket" "app_public_files" {
  bucket        = "${local.prefix}-files"
  acl           = "public-read"
  region        = "ap-northeast-1"
  force_destroy = true
}