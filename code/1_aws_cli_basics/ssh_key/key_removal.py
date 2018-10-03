import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print(response)

response = ec2.delete_key_pair(KeyName='TestKey')
print(response)
