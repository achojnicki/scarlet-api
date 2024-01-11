from response import Response

class delivery_addresses:
    def delivery_addresses(self, session_uuid, page=1, **kwargs):
        rsp=Response()
        
        session=self._middlewares.sessions.get_session_by_session_uuid(
            session_uuid=session_uuid)
        
        addresses=self._middlewares.users.get_user_addresses(
            user_uuid=session['user_uuid'],
            page=page
            )
        
        rsp.status="Success"
        rsp.message="Delivery Addresses"
        rsp.data=addresses
        
        return rsp