                ######################################

import boto3
contents = []
ec2 = boto3.resource('ec2', region_name='us-east-1')
print(ec2)
for instance in ec2.instances.all():
    contents.append(instance.id)
print('\nContents:',contents)
client = boto3.client('ec2', region_name='us-east-1')

val = ec2.instances.filter(InstanceIds=contents)
print('Val:',val)
id_list = []
for i in val:
    print('\ni.tags for',i.id + ':', i.tags)
    if i.tags != None:
        for tagdict in i.tags:
            print('i.id for', tagdict['Value'] +':', i.id)
            if tagdict['Key'].lower() == 'project' and tagdict['Value'].lower()[0:4]!= 'test':
                id_list.append(i.id)

    else:
        id_list.append(i.id)
        print('i.id for None:',i.id)
print('\nid_list:',id_list,'\n')
#client.stop_instances(InstanceIds=id_list)
print("stopping Instance with 'id':", id_list)
if len(id_list) is None:
    print("No Instance Terminatedd")
    

########################################################
import boto3
import s3fs
from smart_open import open
import pandas as pd
def lambda_handler(event, context):
    contents = []
    path = 's3://test-golu/sam.csv'
    df = pd.read_csv(open(path))
    print(df)

    ec2 = boto3.resource('ec2', region_name='us-east-1')
    client = boto3.client('ec2', region_name='us-east-1')
    status = []
    id_list = []

    for ii in df['Id']:
        print('ii:',ii)
        contents.append(ii)
        try:
            val = ec2.instances.filter(InstanceIds=contents)
            for i in val:
                if i.tags != None:
                    for tagdict in i.tags:
                        if tagdict['Key'].lower() == 'project' and tagdict['Value'].lower()[0:4]!= 'test':
                            id_list.append(i.id)
                            status.append('this instance is deleted')
                        else:
                            status.append('condition can\'t be satisfied')
                        print(status,'\n')
        except:
            status.append('This id does not exist')
            print(status,'\n')
        contents = []

    print('\nid_list:',id_list,'\n')
    # client.stop_instances(InstanceIds=id_list)
    print("stopping Instance with 'id':", id_list)
    if len(id_list) is None:
        print("No Instance Terminatedd")

    print('Status:',status)
    print('Status len:',len(status))
    df['Status']=status
    print(df)
    bytes_to_write = df.to_csv(header=True, index=False).encode()
    fs = s3fs.S3FileSystem()
    with fs.open('s3://test-golu/samlp.csv', 'wb') as f:
        f.write(bytes_to_write)
