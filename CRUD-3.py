from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations from Animal collection in MongoDB """
    
    def __init__(self, USER = 'aacuser', PASS = 'SNHU1234'):
        # Connection Variables
        
        self.USER = USER
        self.PASS = PASS
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31225
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST,
                                                             PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
    #C in CRUD
    
    def create(self, data) -> bool:
        if data is not None and isinstance(data, dict): 
        # Checks that param is present and is a dictionary
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, "
                            "because data parameter is invalid.")
            return False
        
    # R in CRUD    
    def read(self, query) -> list:
        result = [] # Creates empty list to return if query is invalid
        if query is not None and isinstance(query, dict):
            cursor = self.database.animals.find(query)
            results = list(cursor) # Converts cursor to a list
            return results
        else:
            return result # Returns empty list
        
    # U in CRUD
    def update(self, old, new, multiple=False) -> int: 
        # Has param 'multiple' to be set true by user if wanting to update many
        if (old is not None and isinstance(old, dict) and 
            new is not None and isinstance(new, dict)):
            if multiple:
                result = self.database.animals.update_many(old, {'$set': new})
            else:
                result = self.database.animals.update_one(old, {'$set': new})
            return result.modified_count # Return number of entries modified
        else:
            raise Exception("Parameters must be non-empty dictionaries.")
        
    # D in CRUD
    def delete(self, entry, multiple=False) -> int:
        # Has param 'multiple' to be set true by user if wanting to delete many
        if entry is not None and isinstance(entry, dict):
            if multiple:
                result = self.database.animals.delete_many(entry)
            else:
                result = self.database.animals.delete_one(entry)
            return result.deleted_count # Return number of entries deleted
        else:
            raise Exception("Parameter must be a non empty dictionary.")
