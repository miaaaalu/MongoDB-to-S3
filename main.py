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
