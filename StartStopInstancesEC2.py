# Funcao Start Stop para uso com servico EC2 AWS em conjunto com servico Cloud Watch AWS e Lambda AWS
# Biclioteca AWS
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html#Using_ChangingAttributesWhileInstanceStopped
# https://aws.amazon.com/pt/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client

import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    try:
        start_stop_ec2_instances(event, context)
        
        start_stop_rds_instances(event, context)
        
    except Exception as e:
            displayException(e)
            traceback.print_exc()
            
def start_stop_ec2_instances(event, context):
    
    # Get action parametro para event
    action = event.get('action')
    
    if action is None:
        action = ''

    # Checando action
    if action.lower() not in ['start', 'stop']:
        print ("A Funcao nao esta operando e sera abortada")
    else:
        # Get ec2 com filter conditions
        filtered_ec2 = ec2.describe_instances(
            Filters=[
                {'Name': 'tag-key', 'Values': ['Auto-StartStop-Enabled', 'auto-startstop-enabled']},
                {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
            ] # Condicoes adicionadas nas TAG's dos servicos AWS - Trigger 
        ).get(
            'Reservations', []
        )
    
        # Convertendo array of array para uma flat array
        instances_ec2 = sum(
            [
                [i for i in r['Instances']]
                for r in filtered_ec2
            ], [])
    
        print ("Encontrada " + str(len(instances_ec2)) + " EC2 instances started/stopped")
    
        # Loop through instances
        for instance_ec2 in instances_ec2:

            try:
                instance_id = instance_ec2['InstanceId']

                # ec2 instance TAG name
                for tag in instance_ec2['Tags']:
                    if tag['Key'] == 'Name':
                        instance_name = tag['Value']
                        print ("instance_name: " + instance_name + " instance_id: " + instance_id)
                        continue
                    
                # ec2 instance STATUS
                instance_state = instance_ec2['State']['Name']
                print ("STATUS: %s" % instance_state)
                
                # Start or stop ec2 instance
                if instance_state == 'running' and action == 'stop':
                    ec2.stop_instances(
                        InstanceIds=[
                            instance_id
                            ],
                        # DryRun = True
                        )
                    print ("Instance %s comes to stop" % instance_id)
                    
                elif instance_state == 'stopped' and action == 'start':
                    ec2.start_instances(
                        InstanceIds=[
                            instance_id
                            ],
                        # Se funcionamento ok = true
                        )
                    print ("Instance %s" % instance_id)
                    
                else: #Não esta pronta para funcao
                    print ("Instance %s(%s) Funcao não pronta" % (instance_id, instance_name))
                
            except Exception as e:
                displayException(e)

