import json
import boto3


print('Loading function')


def lambda_handler(event, context):
    # enhance the code to set default values
    # default env_value = Dev
    env_value = event['tagname']
    # default env_name = env
    env_name = event['tagvalue']
    # default action = stop
    action = event["action"] 
    ec2_resource = boto3.resource('ec2')
    instance_ids = []
    for instance in ec2_resource.instances.all():
        for name_pair in instance.tags:
            if env_name in name_pair.values() and env_value in name_pair.values():
                instance_ids.append(instance.id)
                if action == "stop":
                    instance.stop()
                elif action == "start":
                    instance.start()
                elif action == "delete":
                    instance.terminate()
                elif action == "reboot":
                    instance.reboot()
                else:
                    instance.reload()

    return instance_ids
    #raise Exception('Something went wrong')