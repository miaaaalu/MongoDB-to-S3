def check_existence_collection(collection_name, db_name, client):
    if db_name in client.list_database_names():
        db = client[db_name]
        if collection_name in db.list_collection_names():
            collection_lists = db[collection_name]
            print(f'Collection: {collection_name} in Database: {db_name} exists')
        else:
            print(f'Collection: {collection_name} in Database: {db_name} does not exists') 
    else:
        print(f'{db_name} does not exist')
    return collection_lists