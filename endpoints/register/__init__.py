from response import Response
from exceptions import UserAlreadyExists

class register:
    def register(self, user_emal:str, user_password:str, forename: str, surname: str, address_first_line:str, address_second_line:str, town:str, postcode:str,  **kwargs):
        rsp=Response()

        

        try:
            user=self._middlewares.users.register_user(
                user_email=user_emal,
                user_password=user_password,
                forename=forename,
                surname=surname,
                address_first_line=address_first_line,
                address_second_line=address_second_line,
                town=town,
                postcode=postcode
                )
            
            rsp.status="Success"
            rsp.message="User registration succeeded."

        except UserAlreadyExists:
            rsp.status="Error"
            rsp.message="User with this email already exists. Try different email address."

        except PasswordDoNotMatchCriteria as e:
            rsp.status="Error"
            rsp.message="Password do not match criteria."
            rsp.data=e.data

        except AddressDoNotMatchCriteria as e:
            rsp.status="Error"
            rsp.message="Address do not match criteria."
            rsp.data=e.data

        return rsp