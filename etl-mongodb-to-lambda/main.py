import os
from dotenv import load_dotenv
from pymongo import MongoClient

from botocore.exceptions import ClientError
import json
from bson.json_util import dumps
import os
from dotenv import load_dotenv
from datetime import datetime
import datetime

#####################
#####################Preparation#####################
#####################

# set env
load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')

# Connection to the MongoDB Server
mongodb_client = MongoClient(MONGODB_URI)

# Database Name 
mongo_database = mongodb_client[MONGODB_DATABASE]

# Fetch Data 
# Collection Name

for table_name in required_collection.keys():
    data_collection = get_collection(mongodb_client, os.environ['MONGODB_DATABE'], table_name)
    filtered_data = required_data[table_name]
    data_json = filtered_data(data_collection)
    try:
        upload_s3(s3_client, data_json, os.environ['LOAD_BUCKET_NAME'], "{0}.json".format(table_name))
        print('{0}.json has been upload to S3'.format(table_name))
    except Exception as error:
        print(error)

# item_details_2 = database_collection_cities.find()
# for item in item_details_2.limit(2):
   #  print(item)
