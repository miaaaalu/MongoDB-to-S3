import json
from bson.json_util import dumps

def jobcategories_filter(collection):
	#retrieve id, key, name and _v fields only
	jobcategories_data = collection.find(
		{},
		{'_id': 1, 'key': 1, 'name': 1, '__v': 1}
	)
	jobcategories_json = json.loads(dumps(jobcategories_data))
	print('jobcategories json file created')
	return jobcategories_json

def cities_filter(collection):
    #retrieve id, country, name and chName fields only
    cities_data = collection.find(
        {},
        { 
            '_id': 1,
            'country': 1,
            'name': 1,
            'chName': 1, 
        }
    )
    cities_json = json.loads(dumps(cities_data))
    print('cities json file created')
    return cities_json

def jobs_filter(collection):
    job_data = collection.aggregate([
        {
            #retrieve the detail category of this job from jobcategories table, and name the field as categories_list locally
            '$lookup': {
                'from': 'jobcategories',
                'localField': 'categories',
                'foreignField': '_id',
                'as': 'categories_list'
            }
        },
        {
            #retrieve specific name of the city from cities table, and name the field as city locally
            '$lookup':{
                'from': 'cities',
                'localField': 'city',
                'foreignField': '_id',
                'as': 'cities'
            }
        },
        {
            #retreive the following fields only, denoted as 1
            '$project': {
                '_id': 1,
                'title': 1,
                'publishedDate': 1,
                'deadline': 1,
                'effictivePeriod': 1,
                'jobRequiredDegree': 1,
                'level': 1,
                'jobType': 1,
                'city': '$cities.name',
                'country': 1,
                'categories_list': '$categories_list.key'
            }
        }
    ])
    jobs_json = json.loads(dumps(job_data))
    print('jobs json file created')
    return jobs_json

def users_filter(collection):
    user_data = collection.aggregate([
        {
            #retrieve city name according to local city object ID from cities table
            '$lookup': {
                'from': 'cities',
                'localField': 'city',
                'foreignField': '_id',
                'as': 'cities'
            }
        },
        { 
            #retrieve the follwing fields only
            '$project': {
                '_id': 1,
                'interestedFields': 1,
                'jobStatus': 1,
                'degree': 1,
                'currentStatus': 1,
                'gender': 1,       
                "cities.name": 1,
                "city": '$cities.name',           
        }
    }
    ])
    users_json = json.loads(dumps(user_data))
    print('users json file created')
    return users_json