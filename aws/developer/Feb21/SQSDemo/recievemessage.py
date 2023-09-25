import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue by name
queue = sqs.get_queue_by_name(QueueName='learningthoughts_order_queue')

for message in queue.receive_messages():
    print(message.body)