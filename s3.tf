resource "aws_s3_bucket" "json_bucket" {
  bucket_prefix = "json-bucket"
}


resource "aws_s3_object" "json-parquet" {
  bucket = aws_s3_bucket.json_bucket.id
  key = "json-parquet.zip"
  source = "${path.module}/json-parquet.zip"
}
