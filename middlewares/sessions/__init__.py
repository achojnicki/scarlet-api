class Sessions:
	def __init__(self, root):
		self._root = root

		self.config = self._root.config
		self.log = self._root.log
		self.db = self._root.db

	def get_session_by_session_uuid(self, session_uuid):
		session=self.db.get_session_by_session_uuid(session_uuid)

		del session['_id']

		self.log.success('Obtained session')
		return session