import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
# VPC's
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
# Get VPC Ids
try:
# Grupo de Seguranca
    response = ec2.create_security_group(GroupName='SECURITY_GROUP_NAME',
                                         Description='DESCRIPTION',
                                         VpcId=vpc_id)
# Seguranca
    security_group_id = response['GroupId']
    print('Grupo de Seguranca criado %s em VPC %s.' % (security_group_id, vpc_id))
    # configure your security rules
    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80, #incoming 80
             'ToPort': 80,   #forwarding 80
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}, #Ip ranges
            {'IpProtocol': 'tcp', #Protocolos usados
             'FromPort': 22, # SSH
             'ToPort': 22, 
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    print('Progresso %s' % data) #
except ClientError as e:
    print(e)
