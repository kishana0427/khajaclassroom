import json
import boto3

ec2 = boto3.client('ec2')

def stop_ec2_instances(tagname, tagvalue):
    """
    This method will get ec2 instances by tag and stops the instances
    """
    response = ec2.describe_instances(Filters=[
        {
            'Name': f'tag:{tagname}',
            'Values':  [ tagvalue ]
        }
    ])
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    ec2.stop_instances(InstanceIds = instance_ids)
    return instance_ids


def lambda_handler(event, context):
    """
    This function is lambda handler function 
    :param event: This consists of the data passed by the user
    :param context: This object consists of context information of the execution environment
    """
    if 'tagname' not in event and 'tagvalue' not in event:
        raise KeyError('tagname and tagvalue key are manadatory in the event object')
    tag_name = event['tagname']
    tag_value = event['tagvalue']
    instance_ids = stop_ec2_instances(tag_name, tag_value)
    for instance_id in instance_ids:
        print(f"This instance with {instance_id} is shutting down")
    


