"""
- Author : Kishor D
- Info   : List Blockchain Networks you created
"""

import boto3
import json

def list_networks(client):
    response = client.list_networks()
    print (json.dumps(response, indent=1, default=str))

if __name__ == "__main__":
    client = boto3.client('managedblockchain', region_name='us-east-1')
    list_networks(client)


'''
RESPONSE OUTPUT:
{
 "ResponseMetadata": {
  "RequestId": "32d990c6-30a9-4d99-ab00-65615a02fafa",
  "HTTPStatusCode": 200,
  "HTTPHeaders": {
   "date": "Fri, 18 Mar 2022 15:37:12 GMT",
   "content-type": "application/json",
   "content-length": "386",
   "connection": "keep-alive",
   "x-amzn-requestid": "32d990c6-30a9-4d99-ab00-65615a02fafa",
   "x-amz-apigw-id": "PL8OYFxOIAMFefQ=",
   "x-amzn-trace-id": "Root=1-6234a728-639c40970014673859d6d90a;Sampled=0"
  },
  "RetryAttempts": 0
 },
 "Networks": [
  {
   "Id": "n-W7ZRD4CMOJCNLKXUPEMTBBACRU",
   "Name": "BlockchainHyperLedgerFabricCLI",
   "Description": "Managed Blockchain Hyper Ledger Fabric Network using CLI",
   "Framework": "HYPERLEDGER_FABRIC",
   "FrameworkVersion": "2.2",
   "Status": "AVAILABLE",
   "CreationDate": "2022-03-18 14:42:41.455000+00:00",
   "Arn": "arn:aws:managedblockchain:us-east-1::networks/n-W7ZRD4CMOJCNLKXUPEMTBBACRU"
  }
 ]
}
'''