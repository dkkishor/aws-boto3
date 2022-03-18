"""
- Author : Kishor D
- Info   : List Blockchain Nodes
"""

import boto3
import json

def list_nodes(client):
    response = client.list_nodes(NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU',
                                 MemberId='m-KKZHPIBHVVDUNOKNJH5LC2D47M')
    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    list_nodes(client)


'''
RESPONSE OUTPUT:
{
 "ResponseMetadata": {
  "RequestId": "7e19cb49-8d7b-4298-abb2-1038e10c4785",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 16:12:24 GMT",
   "content-type": "application/json",
   "content-length": "283",
   "connection": "keep-alive",
   "x-amzn-requestid": "7e19cb49-8d7b-4298-abb2-1038e10c4785",
   "x-amz-apigw-id": "PMBYUGkSoAMFdLQ=",
   "x-amzn-trace-id": "Root=1-6234af68-135354af76c6c6b055afe486;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "Nodes": [
  {
   "Id": "nd-FPHJVSTIXVA27M773D74M66BJE",
   "Status": "CREATING",
   "CreationDate": "2022-03-18 16:11:28.277000+00:00",
   "AvailabilityZone": "us-east-1a",
   "InstanceType": "bc.t3.small",
   "Arn": "arn:aws:managedblockchain:us-east-1:000726156061:nodes/nd-FPHJVSTIXVA27M773D74M66BJE"
  }
 ]
}
'''