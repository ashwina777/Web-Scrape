import pandas as pd
from pymongo import MongoClient

# MongoDB connection details
username = "pwskills"
password = "pwskills"
database_name = "scrapper_eng_pwskills"
collection_name = "scraper_pwskills_eng"
uri = f"mongodb+srv://{username}:{password}@cluster0.hbbfbmr.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(uri)
db = client[database_name]
collection = db[collection_name]

# Fetch all documents from the collection
documents = list(collection.find())

# Convert MongoDB documents to a Pandas DataFrame
df = pd.DataFrame(documents)

# Optionally, remove the MongoDB-generated "_id" field
if "_id" in df.columns:
    df = df.drop(columns=["_id"])

# Save the DataFrame to a CSV file
csv_filename = "mongodb_collection.csv"
df.to_csv(csv_filename, index=False)

print(f"Collection data saved to {csv_filename}")
