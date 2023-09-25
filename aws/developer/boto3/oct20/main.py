import boto3

client = boto3.client('s3')


def populate_s3_buckets():
    """
    This method will print all the s3 buckets
    """
    bucket_dict = client.list_buckets()
    for bucket in bucket_dict['Buckets']:
        print(bucket['Name'])


if __name__ == "__main__":
    populate_s3_buckets()
