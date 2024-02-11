import os
import boto3
# Set up environment variables
os.system("setx AWS_SECRET_ACCESS_KEY your_secret_access_key")
os.system("setx AWS_ACCESS_KEY_ID your_access_key_id")

# Get the secret key and access key
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
access_key = os.getenv('AWS_ACCESS_KEY_ID')
# Create a connection to EC2
ec2 = boto3.client('ec2',
                   region_name='us-east-1',
                   aws_access_key_id=access_key,
                   aws_secret_access_key=secret_key)

# Delete the instances
ec2.terminate_instances(InstanceIds=['i-0a315ded38c3b603b'])

# Delete the subnet
ec2.delete_subnet(SubnetId='subnet-05d86326648d4dbdd')

# Delete the VPC
ec2.delete_vpc(VpcId='vpc-0b99f45cdcafc35c8')