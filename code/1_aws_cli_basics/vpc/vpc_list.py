import boto3
client = boto3.client('ec2')

result = client.describe_security_groups()
for value in result["SecurityGroups"]:
    print(value["GroupId"])
    print(value["VpcId"])
