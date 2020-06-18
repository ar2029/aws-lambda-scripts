# lis = [1,2,3,5,7,11,13,17,19]
# # b = [1,2,3,5,7,11,13,17,19]
# a = [4,6,8,9,10,12,14,15,16,18,20,21]
# usr = int(input('Enter the number '))
# for i in range(1,1000000):
#     for n in range(2, 20):
#         if i % n == 0:
#             a += [i]
#
#  # for k in range(11,10000000000000000):
# if usr not in a or usr in lis :
#     print("Prime")
# else:
#     print("Not Prime")


# c =[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
# 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
# 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367,
# 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
#
# if b == c:
#     print(True)
# else:
#     print(False)

# n = int(input('Enter the no.: '))
# for i in range(1,n):ḍ
#     n = n * i
# print(n)


# n = int(input('enter the number '))
#
# a = True
# for i in range(2,n//2):
#     if n % i == 0:
#         a = False
#         break
#
# if a == True:
#     print(a)
# else:
#     print(a)


# for j in range(5,1,-1):
#     for i in range(j):
#         print('*',end='')
#     print()



# i=1
# k=1
# while(i<=10):
#     for j in range (k):
#         print(i,end="")
#         i=i+1
#     print()
#     k=k+1


# for i in range(10):
#     for j in range(i):
#         print(i,end='')
#     print()


# for i in range(1,10):
#     for j in range (i):
#         print('c',end='')
#     for k in range(10,14):
#         print('*', end='')
#     print()


# for i in range

# n=5
# for i in range(5):
#     for j in range(i):
#         print(' ',end='')
#     for k in range(n):
#         print('*',end='')
#     print()
#     n=n-1


# a = 10
# b = 2
# c = 3

# if a<b and a<c:
#     print('Greater is a')

# elif b>c and b>a:
#     print('Greater is b')

# else:
#     print('Greater is c')

# if(a > b):
#     if( a > c):
#         print("a is big brother")
#     else:
#          print ("c is big brother")
# else:
#     if(b>c):
#         print("b is big brother")
#     else:
#         print("c is big brother")

# a = [70, 1, 11, 17, 28, 7, 25, 23, 21, 33, 12]
# for i in range(11):
#     for j in range(11):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j],a[i]
# print(a)
# print(a[j])


# a = [70, 1, 11, 17, 28, 7, 25, 23, 21, 33, 12]
# for i in range(11):
#     print (a[i],end='')
#     print()
#     for j in range(11):
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
        # print(a[j])
    # print()
# print(a)
# for i in range(11):

    # print(a[i])

# n = 7
# k = '*'
# for i in range(n):
#     print(k, end=' ')
#     # k += 1
# print()
# for l in range(n-2):
#     for i in range(n):
#         print(k, end=' ')
#         # k += 1
#     print()
#     for j in range(n-2):
#         print(k, end=' ')
#         # print(' ',end='')
#     print(k)
#     # k += 1
# for i in range(n):
#     print(k,end=' ')
#     # k += 1
                
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