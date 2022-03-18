"""
- Author : Kishor D
- Info   : Get a specific Node Details for a Member Under Blockchain Network
"""

import boto3
import json

def get_node(client):
    response = client.get_node(
        NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU',
        MemberId='m-KKZHPIBHVVDUNOKNJH5LC2D47M',
        NodeId='nd-FPHJVSTIXVA27M773D74M66BJE'
    )

    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name = 'us-east-1')
    get_node(client)


'''
RESPONSE:
{
 "ResponseMetadata": {
  "RequestId": "6d3cc17a-889f-4750-b586-52fe44a89f2f",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 16:37:09 GMT",
   "content-type": "application/json",
   "content-length": "906",
   "connection": "keep-alive",
   "x-amzn-requestid": "6d3cc17a-889f-4750-b586-52fe44a89f2f",
   "x-amz-apigw-id": "PMFAZFWFIAMF4NQ=",
   "x-amzn-trace-id": "Root=1-6234b535-661d9624670b693436de3912;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "Node": {
  "NetworkId": "n-W7ZRD4CMOJCNLKXUPEMTBBACRU",
  "MemberId": "m-KKZHPIBHVVDUNOKNJH5LC2D47M",
  "Id": "nd-FPHJVSTIXVA27M773D74M66BJE",
  "InstanceType": "bc.t3.small",
  "AvailabilityZone": "us-east-1a",
  "FrameworkAttributes": {
   "Fabric": {
    "PeerEndpoint": "nd-fphjvstixva27m773d74m66bje.m-kkzhpibhvvdunoknjh5lc2d47m.n-w7zrd4cmojcnlkxupemtbbacru.managedblockchain.us-east-1.amazonaws.com:30003",
    "PeerEventEndpoint": "nd-fphjvstixva27m773d74m66bje.m-kkzhpibhvvdunoknjh5lc2d47m.n-w7zrd4cmojcnlkxupemtbbacru.managedblockchain.us-east-1.amazonaws.com:30004"
   }
  },
  "LogPublishingConfiguration": {
   "Fabric": {
    "ChaincodeLogs": {
     "Cloudwatch": {
      "Enabled": true
     }
    },
    "PeerLogs": {
     "Cloudwatch": {
      "Enabled": true
     }
    }
   }
  },
  "StateDB": "CouchDB",
  "Status": "AVAILABLE",
  "CreationDate": "2022-03-18 16:11:28.277000+00:00",
  "Tags": {},
  "Arn": "arn:aws:managedblockchain:us-east-1:000726156061:nodes/nd-FPHJVSTIXVA27M773D74M66BJE",
  "KmsKeyArn": "AWS_OWNED_KMS_KEY"
 }
}
'''