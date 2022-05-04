def get_database():
    from pymongo import MongoClient
    import pymongo
    import os
    from dotenv import load_dotenv

    load_dotenv()
    MONGODB_URI = os.getenv('MONGODB_URI')
    MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(MONGODB_URI)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[MONGODB_DATABASE]
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()