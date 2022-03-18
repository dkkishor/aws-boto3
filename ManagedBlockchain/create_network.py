"""
- Author : Kishor D
- Info   : Create Blockchain HyperLedger Fabric Network
"""

import boto3
import json

def create_network(client):
    response = client.create_network(
        Name='BlockchainHyperLedgerFabricCLI',
        Description='Managed Blockchain Hyper Ledger Fabric Network using CLI',
        Framework='HYPERLEDGER_FABRIC',
        FrameworkVersion='2.2',
        FrameworkConfiguration={
            'Fabric': {
                'Edition': 'STARTER'
            }
        },
        VotingPolicy={
            'ApprovalThresholdPolicy': {
                'ThresholdPercentage': 50,
                'ProposalDurationInHours': 24,
                'ThresholdComparator': 'GREATER_THAN_OR_EQUAL_TO'
            }
        },
        MemberConfiguration={
            'Name': 'FabricCLIMember1',
            'Description': 'FabricCLIMember1',
            'FrameworkConfiguration': {
                'Fabric': {
                    'AdminUsername': 'admin',
                    'AdminPassword': 'AdminPass1'
                }
            },
            'LogPublishingConfiguration': {
                'Fabric': {
                    'CaLogs': {
                        'Cloudwatch': {
                            'Enabled': True
                        }
                    }
                }
            }
        }
    )

    print (json.dumps(response, indent=1))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    create_network(client)



'''
RESPONSE OUTPUT:
{
 "ResponseMetadata": {
  "RequestId": "6dcb0455-3f1f-4c7c-b020-5b8299ae3408",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 14:42:41 GMT",
   "content-type": "application/json",
   "content-length": "86",
   "connection": "keep-alive",
   "x-amzn-requestid": "6dcb0455-3f1f-4c7c-b020-5b8299ae3408",
   "x-amz-apigw-id": "PL0PJFXzoAMF6YA=",
   "x-amzn-trace-id": "Root=1-62349a60-156a34f23546006d6f3e1515;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "NetworkId": "n-W7ZRD4CMOJCNLKXUPEMTBBACRU",
 "MemberId": "m-KKZHPIBHVVDUNOKNJH5LC2D47M"
}
'''