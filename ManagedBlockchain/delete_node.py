"""
- Author : Kishor D
- Info   : Delete Node from a Member Under Blockchain HyperLedger Fabric Network
"""

import boto3
import json

def delete_node(client):
    response = client.delete_node(
        NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU',
        MemberId='m-KKZHPIBHVVDUNOKNJH5LC2D47M',
        NodeId='nd-FPHJVSTIXVA27M773D74M66BJE'
    )

    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name = 'us-east-1')
    delete_node(client)


'''
RESPONSE:
{
 "ResponseMetadata": {
  "RequestId": "2514250f-ce19-42d3-9840-5e9fff269ab7",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 16:42:44 GMT",
   "content-type": "application/json",
   "content-length": "2",
   "connection": "keep-alive",
   "x-amzn-requestid": "2514250f-ce19-42d3-9840-5e9fff269ab7",
   "x-amz-apigw-id": "PMF0qGoeIAMFrWg=",
   "x-amzn-trace-id": "Root=1-6234b684-06ad12620013322812c8819f;Sampled=0"
  },
  "RetryAttempts": 0
 }
}
'''