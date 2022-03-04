# Hands-On on calling AWS API's using boto3 (Python SDK for AWS)

### Code Environment
There are many ways to run your code to call various AWS API's using "boto3" python library
1. Local Laptop or PC
2. EC2 instance (Virtual Machine) on AWS

I chose **#2** because I can access this instance from anywhere and not tied to a single pc or laptop.

### Beware of the following
* The costs involved with keeping your instances running.
* Shutdown the instance when not running to reduce the costs.
* Note that you cannot terminate the instnce which will delete the instance and instance volume / storage permanently.

### Launching an EC2 instance
* Login to Management Console and launch an EC2 instance using Linux AMI.
* Select all options which are Free Tier eligible unless you have a need for more resources than what is provided in Free Tier - I chose "t2.micro" instance type.
* I chose default VPC provided by AWS.
* Under "Security Groups" in your default VPC, make sure there is an inbound rule to port 22 so that you can connect to your EC2 instance using SSH.
* Generate key-pair and save the ".pem" file. In my case I saved it as "aws-boto3.pem"

### Connect to EC2 instance and install boto3 python library

SSH to EC2 instance
```ssh -i "aws-boto3.pem" ec2-user@<Public IPv4 DNS Address of EC2 Instance>```

Install "boto3" in EC2 using the steps mentioned in 
[Python Package Index for boto3](https://pypi.org/project/boto3/)
