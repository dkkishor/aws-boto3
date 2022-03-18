"""
- Author : Kishor D
- Info   : Delete a Member Under Blockchain Network
"""

import boto3
import json

def delete_member(client):
    response = client.delete_member(
        NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU',
        MemberId='m-KKZHPIBHVVDUNOKNJH5LC2D47M'
    )

    print (json.dumps(response, indent=1, default=str))
    
if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    delete_member(client)


'''
RESPONSE:
{
 "ResponseMetadata": {
  "RequestId": "82c5ca32-00d4-4072-9989-2713ea45ba8c",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 16:48:22 GMT",
   "content-type": "application/json",
   "content-length": "2",
   "connection": "keep-alive",
   "x-amzn-requestid": "82c5ca32-00d4-4072-9989-2713ea45ba8c",
   "x-amz-apigw-id": "PMGpfEpDIAMFoIQ=",
   "x-amzn-trace-id": "Root=1-6234b7d6-6a5e6bde52cc17e02494efde;Sampled=0"
  },
  "RetryAttempts": 0
 }
}
'''