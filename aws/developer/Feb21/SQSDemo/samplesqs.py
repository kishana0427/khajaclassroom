import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the Queue instance
queue = sqs.get_queue_by_name(QueueName='learningthoughts_order_queue')
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# lets send a message to the queue
response = queue.send_message(MessageBody='Hello World')

for sqsqueue in sqs.queues.all():
    print(sqsqueue.url)