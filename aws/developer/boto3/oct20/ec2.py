import boto3

ec2 = boto3.resource('ec2')


def create_ec2(keypair_name, image_id="ami-07a29e5e945228fa1", instance_type="t2.micro"):
    """
    This method creates the ec2 instance
    :param keypair_name: key pair name
    :param image_id: image id of the ec2 instance
    :param instance_type: size of the ec2
    :return:
    """
    instances = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        NetworkInterfaces=[{
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0
        }],
        MinCount=1,
        MaxCount=1,
        KeyName=keypair_name
    )
    for instance in instances:
        print(instance)
        print(type(instance))


def count_ec2_instances(func):
    def ec2_instance_count(*args, **kwargs):
        instances = func(*args, **kwargs)
        return len(instances['Reservations'][0]['Instances'])

    return ec2_instance_count


@count_ec2_instances
def instance_details():
    """
    This method will return the ec2 instance details
    :return:
    """
    my_client = boto3.client('ec2')
    instances = my_client.describe_instances()
    print(instances)
    return instances


if __name__ == "__main__":
    count = instance_details()
    if count == 0:
        create_ec2(keypair_name='jenkins')
