import boto3

ec2 = boto3.resource('ec2', region_name="ap-southeast-1")

instances = ec2.create_instances(
    NetworkInterfaces=[{'SubnetId': "subnet-beb567da", 'DeviceIndex': 0, 'Groups': ["sg-0d00c869d4d458b07"]}],
	ImageId='ami-0a004f6ff9f98abf8',
	MinCount=1,
	MaxCount=1,
	KeyName="TestKey",
	InstanceType="t2.micro"
)

for instance in instances:
    print(instance.id, instance.instance_type)
