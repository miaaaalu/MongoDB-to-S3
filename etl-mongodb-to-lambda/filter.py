import json
from bson.json_util import dumps

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

    # opton 1
    # for doc in user_data:
    #     print(doc)

    # option 2 
    print('users json file created')
    return(list(user_data)[0])

    # option 3
    # users_json = json.loads(dumps(user_data))
    # print('users json file created')
    # print(user_data)
