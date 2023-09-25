import boto3

my_s3 = boto3.resource('s3')

# print all the bucket names
for bucket in my_s3.buckets.all():
    print("name = {0} created = {1}".format(bucket.name,bucket.creation_date))

# get all the ec2 instances
my_ec2 = boto3.resource('ec2')
print("**********************************************")
print("ec2 details")
print("**********************************************")

for ec2 in my_ec2.instances.all():
    print("Instance id= {0} public ip = {1}".format(ec2.instance_id, ec2.public_ip_address))