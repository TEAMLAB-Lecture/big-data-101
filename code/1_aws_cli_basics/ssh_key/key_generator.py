import boto3

ec2 = boto3.resource('ec2', region_name="ap-southeast-1")

outfile = open('TestKey.pem','w')
key_pair = ec2.create_key_pair(KeyName='TestKey')
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)
