from http import client
import boto3

def start_ec2(region, instance_ids):
    """
    This method is used to start the ec2 instances by region and ids
    """
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.start_instances(InstanceIds=instance_ids)
    print(response)

def stop_ec2(region, instance_ids):
    """
    This method is used to stop the ec2 instances by region and ids
    """
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.stop_instances(InstanceIds=instance_ids)
    print(response)

def start_instances_by_tag(region, tag_name, tag_value):
    """
    This method will find the instances in a region
    """
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances(Filters=[
        {
            'Name': f'tag:{tag_name}',
            'Values': [tag_value]
        }
    ])
    instances_found = response['Reservations'][0]['Instances']
    print(f"found {len(instances_found)} instances")
    #for instance in response['Reservations'][0]['Instances']:
    #    ec2.start_instances(InstanceIds=[instance['InstanceId']])
    instance_ids = [ instance['InstanceId'] for instance in response['Reservations'][0]['Instances']]
    response = ec2.start_instances(InstanceIds=instance_ids)
    print(response)

def stop_instances_by_tag(region, tag_name, tag_value):
    """
    This method will find the instances in a region
    """
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances(Filters=[
        {
            'Name': f'tag:{tag_name}',
            'Values': [tag_value]
        }
    ])
    instances_found = response['Reservations'][0]['Instances']
    print(f"found {len(instances_found)} instances")
    #for instance in response['Reservations'][0]['Instances']:
    #    ec2.start_instances(InstanceIds=[instance['InstanceId']])
    instance_ids = [ instance['InstanceId'] for instance in response['Reservations'][0]['Instances']]
    response = ec2.stop_instances(InstanceIds=instance_ids)
    print(response)



if __name__ == '__main__':
    #stop_ec2(region='us-west-2', instance_ids=["i-0bb52cd3a3a04b4f1"])
    start_instances_by_tag(region="us-west-2", tag_name="env", tag_value="dev")