import boto3

region = 'us-east-1'  # Replace with your actual region
instances = ['i-0f624932c6dd50ed7']  # Replace with your actual instance ID
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('Started your instances: ' + str(instances))