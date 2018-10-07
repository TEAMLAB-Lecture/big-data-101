import boto3

ec2 = boto3.resource('ec2', region_name="ap-southeast-1")

client = boto3.client('ec2', region_name="ap-southeast-1")
instances = client.describe_instances()

for instance in instances["Reservations"]:
  instance_id = instance['Instances'][0]['InstanceId']
  name = "Image for instance {instance_id}".format(instance_id=instance_id)
  print ("creating image for instance {instance_id}".format(instance_id=instance_id))
  client.create_image(InstanceId=instance_id,Name=name)

