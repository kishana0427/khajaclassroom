import boto3

ec2_resource = boto3.resource('ec2')

for instance in ec2_resource.instances.all():
    for name_pair in instance.tags:
        if 'Dev' in name_pair.values():
            instance.stop()