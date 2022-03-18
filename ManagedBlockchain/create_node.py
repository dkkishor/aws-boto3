"""
- Author : Kishor D
- Info   : Create Node Under Blockchain HyperLedger Fabric Network Member
"""

import boto3
import json

def create_node(client):
    response = client.create_node(
        NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU',
        MemberId='m-KKZHPIBHVVDUNOKNJH5LC2D47M',
        NodeConfiguration={
            'InstanceType': 'bc.t3.small',
            'AvailabilityZone': 'us-east-1a',
            'LogPublishingConfiguration': {
                'Fabric': {
                    'ChaincodeLogs': {
                        'Cloudwatch': {
                            'Enabled': True
                        }
                    },
                    'PeerLogs': {
                        'Cloudwatch': {
                            'Enabled': True
                        }
                    }
                }
            },
            'StateDB': 'CouchDB'
        }
    );
    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    create_node(client)


'''
RESPONSE OUTPUT:
{
 "ResponseMetadata": {
  "RequestId": "fb01cf57-c70a-4b92-98c6-1425841ac88c",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 16:11:28 GMT",
   "content-type": "application/json",
   "content-length": "42",
   "connection": "keep-alive",
   "x-amzn-requestid": "fb01cf57-c70a-4b92-98c6-1425841ac88c",
   "x-amz-apigw-id": "PMBPXElkIAMFswA=",
   "x-amzn-trace-id": "Root=1-6234af2e-75a8eb357e5deeaa1a3864fe;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "NodeId": "nd-FPHJVSTIXVA27M773D74M66BJE"
}
'''