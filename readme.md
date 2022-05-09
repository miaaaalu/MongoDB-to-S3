# ETL with MongoDB Data in AWS Lambda
![](/Mongodb-s3.jpg)

## Prepare 

### MongoDB
```powershell
1. Install Mongodb https://www.mongodb.com/docs/manual/administration/install-community/
2. Install MongoDB Compass https://www.mongodb.com/docs/compass/current/install/ 
3. Connect to your Environment mongodb+srv://**************************/JR_KEYSTONE_UAT_20210428?retryWrites=true&w=majority 
```
### Python 3.8 for Lambda
Download [Layer](/python_packages.zip) for pre-installed packages. 
```powershell
We’ll use pymongo for interacting with MongoDB and boto3 for uploading the files to S3

1. Update Permissions for your IAM Role
2. Update attached packages in your S3 as Layers
```

S3 
```powershell
1. Create a Load Bucket 
2. Create a Load folder
```

### Main Script 
```py
import boto3
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from extract import get_collection
from transformation import *
from load import upload_s3

# set env
load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')
LOAD_BUCKET_NAME = os.getenv('MONGODB_DATABASE')
LOAD_FOLDER_NAME = os.getenv('LOAD_FOLDER_NAME')

# Connection to the MongoDB Server
mongodb_client = MongoClient(MONGODB_URI)

# Database Name 
mongo_database = mongodb_client[MONGODB_DATABASE]

# Fetch Data 
def lambda_handler(event, context):
	#loop through the required tables, and load to S3
	load_dotenv()
	s3_client = boto3.client('s3')
	required_data = {"users":users_filter, "jobcategories":jobcategories_filter,"jobs":jobs_filter, "cities":cities_filter}
	for table_name in required_data.keys():
		data_collection = get_collection(mongodb_client, mongo_database, table_name)
		filtered_data = required_data[table_name]
		data_json = filtered_data(data_collection)
		try:
			upload_s3(s3_client, data_json, os.environ['LOAD_BUCKET_NAME'], "{0}.json".format(table_name))
			print('{0}.json has been upload to S3'.format(table_name))
		except Exception as error:
			print(error)
```

### Reference 
- How to Use Python with MongoDB https://www.mongodb.com/languages/python 
- How to fetch data from MongoDB using Python? https://www.geeksforgeeks.org/how-to-fetch-data-from-mongodb-using-python/ 
 

