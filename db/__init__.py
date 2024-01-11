from .users import users
from .sessions import sessions
from .products import products
from .products_categories import products_categories

from pymongo import MongoClient

class DB(
    users,
    sessions,
    products,
    products_categories,

):
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log

        self._mongo_cli=MongoClient(
            self.config.mongo.host,
            self.config.mongo.port,
        )

        self._db=self._mongo_cli[self.config.mongo.db]

        self.users=self._db['users']
        self.sessions=self._db['sessions']
        
        self.products=self._db['products']
        self.products_categories=self._db['products_categories']

        self.user_addresses=self._db['addresses']
