import boto3
from botocore.vendored import requests
import os 

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "AMAZON"]
ec2_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "EC2"]


amazon_ips_less_ec2=[]
     
for ip in amazon_ips:
    if ip not in ec2_ips:
        amazon_ips_less_ec2.append(ip)

for ip in amazon_ips_less_ec2: print(str(ip))

# new lamda function edit


""" def lambda_handler(message, subject):
    
    ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
    amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "AMAZON"]
    ec2_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "EC2"]


    amazon_ips_less_ec2=[]
     
    for ip in amazon_ips:
        if ip not in ec2_ips:
            amazon_ips_less_ec2.append(ip)

    for ip in amazon_ips_less_ec2: print(str(ip))
    
    client = boto3.client("sns")
    topic_arn = os.environ["arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged"] 
    response = client.publish(
        TopicArn=topic_arn, Message=str(ip), Subject="ip changed") 
     """

def lambda_handler(event, context):
    result = "Hello World"
    return {
        'statusCode' : 200,
        'body': result
    }
    
        
""" def send_sns(message, subject):
    client = boto3.client("sns")
    topic_arn = os.environ["arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged"]
    response = client.publish(
        TopicArn=topic_arn, Message="ip has changed-take a look!", Subject="ip changed")
    return response
     """
    
        
     
    
    