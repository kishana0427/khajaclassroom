import boto3

ec2 = boto3.client('ec2')

def terminate(func):
    def terminate_func(**kwargs):
        result = func(**kwargs)
        ec2.terminate_instances(InstanceIds = result)
    return terminate_func



@terminate
def get_ec2_by_tag(**kwargs):
    """
    This method will get ec2 instances by tag
    """
    for key, value in kwargs.items():
        response = ec2.describe_instances(Filters=[
            {
                'Name': f'tag:{key}',
                'Values':  value
            }
        ])
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])
        return instance_ids

def stop_ec2_by_tag(**kwargs):
    """
    This method will get the ec2 instances by the tags defined
    """
    for key, value in kwargs.items():
        response = ec2.describe_instances(Filters=[
            {
                'Name': f'tag:{key}',
                'Values':  value
            }
        ])
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])
        ec2.stop_instances(InstanceIds = instance_ids)


if __name__ == "__main__":
    #stop_ec2_by_tag(ENV=["QA","DEV"])
    get_ec2_by_tag(ENV=["QA","DEV","Prod"])
