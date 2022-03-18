"""
- Author : Kishor D
- Info   : Get a specific Member Details Under Blockchain Network
"""

import boto3
import json

def get_member(client):
    response = client.get_member(
        NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU',
        MemberId='m-KKZHPIBHVVDUNOKNJH5LC2D47M'
    )
    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    get_member(client)


'''
RESPONSE:
{
 "ResponseMetadata": {
  "RequestId": "d02a3893-cb72-482c-b242-19bb23a29115",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 16:31:05 GMT",
   "content-type": "application/json",
   "content-length": "615",
   "connection": "keep-alive",
   "x-amzn-requestid": "d02a3893-cb72-482c-b242-19bb23a29115",
   "x-amz-apigw-id": "PMEHfEIVoAMFoXg=",
   "x-amzn-trace-id": "Root=1-6234b3c9-0f6200b900684f203cf4ce64;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "Member": {
  "NetworkId": "n-W7ZRD4CMOJCNLKXUPEMTBBACRU",
  "Id": "m-KKZHPIBHVVDUNOKNJH5LC2D47M",
  "Name": "FabricCLIMember1",
  "Description": "FabricCLIMember1",
  "FrameworkAttributes": {
   "Fabric": {
    "AdminUsername": "admin",
    "CaEndpoint": "ca.m-kkzhpibhvvdunoknjh5lc2d47m.n-w7zrd4cmojcnlkxupemtbbacru.managedblockchain.us-east-1.amazonaws.com:30002"
   }
  },
  "LogPublishingConfiguration": {
   "Fabric": {
    "CaLogs": {
     "Cloudwatch": {
      "Enabled": true
     }
    }
   }
  },
  "Status": "AVAILABLE",
  "CreationDate": "2022-03-18 14:42:41.448000+00:00",
  "Tags": {},
  "Arn": "arn:aws:managedblockchain:us-east-1:000726156061:members/m-KKZHPIBHVVDUNOKNJH5LC2D47M",
  "KmsKeyArn": "AWS_OWNED_KMS_KEY"
 }
}
'''