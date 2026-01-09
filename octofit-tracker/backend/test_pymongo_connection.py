from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Create a test collection and insert a document
test_collection = db['test_collection']
result = test_collection.insert_one({'test': 'mongodb connection successful'})

# Retrieve and print the document
found = test_collection.find_one({'_id': result.inserted_id})
print('Inserted document:', found)

# List all collections in octofit_db
print('Collections in octofit_db:', db.list_collection_names())
