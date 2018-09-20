import boto3

ec2 = boto3.resource('ec2', region_name="ap-southeast-1")

outfile = open('TestKey.pem','w')
key_pair = ec2.create_key_pair(KeyName='TestKey')
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)


instances = ec2.create_instances(
	ImageId='ami-03221428e6676db69',
	MinCount=1,
	MaxCount=5,
	KeyName="TestKey",
	InstanceType="t2.micro"
)

for instance in instances:
    print(instance.id, instance.instance_type)
