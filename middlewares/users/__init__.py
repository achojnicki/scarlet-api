class Users:
	def __init__(self, root):
		self._root = root

		self.config = self._root.config
		self.log = self._root.log
		self.db = self._root.db

	def get_users(self, page):
		limit = self.config.api.results_per_page
		skip = (int(page)-1)*limit

		users = {}
		data = self.db.get_users(limit, skip)

		for item in data:
		    del item['_id']
		    del item['password_hash']

		for user in data:
		    users[user['user_uuid']] = user

		self.log.success('Obtained users.')
		return users

	def get_user(self, user_uuid):
		user=self.db.get_user_by_user_uuid(user_uuid)

		del user['_id']
		del user['password_hash']

		self.log.success('Obtained user')
		return user

	def get_user_address(self, address_uuid):
		address=self.db.get_user_address(
			address_uuid=address_uuid
			)
		del address['_id']
		self.log.success('Obtained user address')
		return 

	def get_user_addresses(self, user_uuid, page):
		limit = self.config.api.results_per_page
		skip = (int(page)-1)*limit

		addresses={}
		data=self.db.get_user_addresses(
			user_uuid=user_uuid,
			limit=limit,
			skip=skip
			)

		for item in data:
		    del item['_id']

		for address in data:
			addresses[address['address_uuid']] = address

		self.log.success('Obtained user addresses')

		return addresses