import boto3

s3 = boto3.client('s3', region_name="ap-southeast-1")
response = s3.create_bucket(
    Bucket='teamlab-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-1'
        }
    )
