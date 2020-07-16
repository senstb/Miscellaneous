import json
import boto3
import time

def lambda_handler(event, context):

   return stabilizeStateMachine()

def stabilizeStateMachine():
    sfnStatus = checkStateMachineStatus()
    waitCount = 0 
    
    #Check to see if Step Functions succeed; after 30 seconds fail out
    while ((sfnStatus != 'SUCCEEDED') or (waitCount > 3)):
        time.sleep(10)
        sfnStatus = checkStateMachineStatus()
        waitCount += 1
    else:
        if ((sfnStatus != 'SUCCEEDED') and (waitCount > 3)):
            return 'Step Function Failed to Stabilize; check execution logs'
        else:
            return 'Step Function succeeded.'

def checkStateMachineStatus():
    # cfnClient = boto3.client('cloudformation', region_name='us-east-1')
    sfnClient = boto3.client('stepfunctions', region_name='us-east-1')
    
    """
    cfnResponseJson = cfnClient.list_stack_set_operations(
        StackSetName='<application name>',
        MaxResults='1'
    )
    """
    
    sfnResponseJson = sfnClient.list_executions(
        stateMachineArn='arn:aws:states:us-east-1:140303719704:stateMachine:LandingZoneLaunchAVMStateMachine',
        maxResults= 1
    )
    
    latestExecutionStatus = sfnResponseJson['executions'][0]['status']
        
    return latestExecutionStatus