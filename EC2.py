# Open a Command Prompt window.
# Use the following command to set an environment variable:
# setx AWS_SECRET_ACCESS_KEY your_secret_access_key
# setx AWS_ACCESS_KEY_ID your_access_key_id

#import os
import boto3

# Set up environment variables
#os.system("setx AWS_SECRET_ACCESS_KEY your_secret_access_key")
#os.system("setx AWS_ACCESS_KEY_ID your_access_key_id")

# Get the secret key and access key
#secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
#access_key = os.getenv('AWS_ACCESS_KEY_ID')

# Create a connection to EC2
ec2 = boto3.client('ec2',
                   region_name='us-east-1',
                   #aws_access_key_id=access_key,
                   #aws_secret_access_key=secret_key
                   )

# Create a new VPC
response_vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = response_vpc['Vpc']['VpcId']
print(f'VPC created with ID: {vpc_id}')

# Create a subnet within the VPC
response_subnet = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock='10.0.1.0/24'
)
subnet_id = response_subnet['Subnet']['SubnetId']
print(f'Subnet created with ID: {subnet_id}')

# Run instances in the created subnet
conn = ec2.run_instances(
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1,
    ImageId="ami-0e731c8a588258d0d",
    SubnetId=subnet_id
)

print(conn)
