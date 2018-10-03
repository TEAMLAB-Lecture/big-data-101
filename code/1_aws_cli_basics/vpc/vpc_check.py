import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-0d00c869d4d458b07'])
    print(response)
except ClientError as e:
    print(e)
