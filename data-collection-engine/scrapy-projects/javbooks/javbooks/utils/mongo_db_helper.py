import pymongo


class MongoDBHelper:
    def __init__(self, collection_name, db_name, host='localhost', port=27017):
        # launch mongo
        self._client = pymongo.MongoClient(host, port)
        # config the db
        self._db = self._client[db_name]
        # config the collection
        self._name = self._db[collection_name]

    def insert_item(self, item):
        self._name.insert_one(item)

    def find_item(self):
        data = self._name.find()
        return data
