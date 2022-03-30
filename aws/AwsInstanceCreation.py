import boto3

def create_ec2_instance():

    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-07465754c59218cdb",
            MinCount=1,
            MaxCount=1,
            InstanceType="t4g.medium",
            KeyName="KEY1"
        )
    except Exception as e:
        print(e)
create_ec2_instance()