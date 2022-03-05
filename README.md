# Hands-On on calling AWS API's using boto3 (Python SDK for AWS)

### Code Environment
There are many ways to run your code to call various AWS API's using "boto3" python library
1. Local Laptop or PC
2. EC2 instance (Virtual Machine) on AWS

I chose **#2** because I can access this instance from anywhere and not tied to a single pc or laptop.

### Beware of the following
* The costs involved with keeping your instances running.
* Shutdown the instance when not using to reduce the costs.
* Note that you do not want to terminate the instnce which will delete the instance and its volume / storage permanently.

### Launching an EC2 instance
* Login to Management Console and launch an EC2 instance using Linux AMI.
* Select all options which are Free Tier eligible unless you have a need for more resources than what is provided in Free Tier - I chose "t2.micro" instance type.
* I chose default VPC provided by AWS.
* Select an IAM role which has access to specific AWS resources that this EC2 instance needs to access.
* Under "Security Groups" in your default VPC, make sure there is an inbound rule to port 22 so that you can connect to your EC2 instance using SSH.
* Generate key-pair and save the ".pem" file. In my case I saved it as "aws-boto3.pem"
* If you haven't selected an IAM role, you can do so by selecting the instance that you created --> Actions --> Security --> Modify IAM Role.

### Connect to EC2 instance and install boto3 python library in a virtual environment

1. SSH to EC2 instance
```ssh -i "aws-boto3.pem" ec2-user@<Public IPv4 DNS Address of EC2 Instance>```
2. Create a new virtual environment for your project
```python3 -m venv aws-boto3```
3. Go into the new virtual environment you created
```cd aws-boto3```
4. Activate the virtual environment
```source ./bin/activate```
5. Install boto3 specific to this new virtual environment
```pip install boto3```

#### Congrtulations! You are ready with your new environment.

#### Let The Fun Begin!

(NOTE: I created one directory per AWS service which has scripts for each API call using boto3 library)
