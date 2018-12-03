from pprint import pprint
import boto3
import logging
client = boto3.client("ec2")

response = client.describe_images(
    Filters=[
        {
            'Name': 'owner-id',
            'Values': [
                '898082745236',
            ],
            'Name': 'name',
            'Values': [
                'Deep Learning*Ubuntu*',
            ]
        },
    ],
    Owners=[
        'amazon',
    ],
)
for image in response['Images']:
    print('ImageName: {},ImageId: {}'.format(image['Name'],image['ImageId']) )
    print('State: {}'.format(image['State']))
    