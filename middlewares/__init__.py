from .auth import Auth
from .products import Products
from .products_categories import Products_Categories
from .users import Users
from .sessions import Sessions

class Middlewares:
	def __init__(self, root):
		self._root=root

		self.auth=Auth(root)
		self.products=Products(root)
		self.products_categories=Products_Categories(root)
		self.users=Users(root)
		self.sessions=Sessions(root)