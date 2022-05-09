from botocore.exceptions import ClientError
import json
import os
from dotenv import load_dotenv
from datetime import datetime
import datetime

def upload_s3(s3_client, data, bucket, file_name):
	#upload the file to S3 specific folder
	load_dotenv()
	date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")   # UTC timestamp
	upload_data = json.dumps(data, ensure_ascii=False)
	key = f"{os.environ['LOAD_FOLDER_NAME']}/{file_name.split('.')[0]}-{date}.json"
	try:
		s3_client.put_object(Bucket=bucket, Key=key, Body=upload_data)
	except ClientError as e:
		error_message = e.response['Error']['Message']
		print(error_message)