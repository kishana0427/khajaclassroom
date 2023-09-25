import boto3

# Get the sns client
sns = boto3.client('sns')
sns.publish(TopicArn='yourtopicarn',
            Message="This is from python code",
            Subject ="From Python")
