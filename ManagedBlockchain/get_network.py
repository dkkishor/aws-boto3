"""
- Author : Kishor D
- Info   : Get a specific Network Details Under Blockchain
"""

import boto3
import json

def get_network(client):
    response = client.get_network(
        NetworkId='n-W7ZRD4CMOJCNLKXUPEMTBBACRU'
    )
    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    get_network(client)


'''
RESPONSE:
{
 "ResponseMetadata": {
  "RequestId": "94c5f75a-0f34-486d-a9a9-ad97c6d6f378",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 16:26:34 GMT",
   "content-type": "application/json",
   "content-length": "806",
   "connection": "keep-alive",
   "x-amzn-requestid": "94c5f75a-0f34-486d-a9a9-ad97c6d6f378",
   "x-amz-apigw-id": "PMDdMEB7IAMFrnw=",
   "x-amzn-trace-id": "Root=1-6234b2ba-2bf38bb6288abe2a5936a999;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "Network": {
  "Id": "n-W7ZRD4CMOJCNLKXUPEMTBBACRU",
  "Name": "BlockchainHyperLedgerFabricCLI",
  "Description": "Managed Blockchain Hyper Ledger Fabric Network using CLI",
  "Framework": "HYPERLEDGER_FABRIC",
  "FrameworkVersion": "2.2",
  "FrameworkAttributes": {
   "Fabric": {
    "OrderingServiceEndpoint": "orderer.n-w7zrd4cmojcnlkxupemtbbacru.managedblockchain.us-east-1.amazonaws.com:30001",
    "Edition": "STARTER"
   }
  },
  "VpcEndpointServiceName": "com.amazonaws.us-east-1.managedblockchain.n-w7zrd4cmojcnlkxupemtbbacru",
  "VotingPolicy": {
   "ApprovalThresholdPolicy": {
    "ThresholdPercentage": 50,
    "ProposalDurationInHours": 24,
    "ThresholdComparator": "GREATER_THAN_OR_EQUAL_TO"
   }
  },
  "Status": "AVAILABLE",
  "CreationDate": "2022-03-18 14:42:41.455000+00:00",
  "Tags": {},
  "Arn": "arn:aws:managedblockchain:us-east-1::networks/n-W7ZRD4CMOJCNLKXUPEMTBBACRU"
 }
}
'''