import boto3
import os

# Create an S3 client
s3 = boto3.client('s3')

bucket_name = 'teamlab-bucket'

files = os.listdir("./")

for filename in files:
  s3.upload_file(filename, bucket_name, filename)
