import pymongo


def database_load(data):
    try:
        # Establish connection to MongoDB
        connection_string = ('mongodb+srv://zayedbinshafi:kxGpejfvpJ4ehenI@projectcluster.gx6e2ja.mongodb.net/'
                             '?retryWrites=true&w=majority&appName=projectCluster')
        client = pymongo.MongoClient(connection_string)
        db = client['sunglasshut']
        collection = db['product_info']

        # Clear existing data in the collection
        collection.delete_many({})

        # Insert new data into the collection
        collection.insert_many(data)

        # Close the connection
        client.close()

        return True, "Data has been successfully loaded into MongoDB."

    except Exception as e:
        return False, f"Error in loading into MongoDB: {e}"
