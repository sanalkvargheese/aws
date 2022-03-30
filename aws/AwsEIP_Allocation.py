import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    allocation = ec2.allocate_address(Domain='vpc')
    response = ec2.associate_address(AllocationId= 'eipalloc-036b7202b1db7ea0d',
                                     InstanceId='i-0275bb768e6bb03b8')
    print(response)
except ClientError as e:
    print(e)