"""
- Author : Kishor D
- Info   : List Blockchain Members
"""

import boto3
import json

def list_members(client):
    response = client.list_members(NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU')
    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    list_members(client)


'''
RESPONSE OUTPUT:
{
 "ResponseMetadata": {
  "RequestId": "d8519afe-1d0d-4e70-ad1c-75a0cdbe83b0",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 15:38:47 GMT",
   "content-type": "application/json",
   "content-length": "299",
   "connection": "keep-alive",
   "x-amzn-requestid": "d8519afe-1d0d-4e70-ad1c-75a0cdbe83b0",
   "x-amz-apigw-id": "PL8dNFi5oAMFWtg=",
   "x-amzn-trace-id": "Root=1-6234a787-29a0eb1173e3d8135df18102;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "Members": [
  {
   "Id": "m-KKZHPIBHVVDUNOKNJH5LC2D47M",
   "Name": "FabricCLIMember1",
   "Description": "FabricCLIMember1",
   "Status": "AVAILABLE",
   "CreationDate": "2022-03-18 14:42:41.448000+00:00",
   "IsOwned": true,
   "Arn": "arn:aws:managedblockchain:us-east-1:000726156061:members/m-KKZHPIBHVVDUNOKNJH5LC2D47M"
  }
 ]
}
'''