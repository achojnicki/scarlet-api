#auth
class AuthException(Exception):
    pass

class UserDoNotExist(AuthException):
    pass

class PasswordDoNotMatch(AuthException):
    pass


#args_validator
class FormValidatorException(Exception):
    pass

class FormDefinitionSyntaxError(FormValidatorException):
    pass

class ValidationError(FormValidatorException):
    pass

class FormNotDefined(FormValidatorException):
    pass


#registration
class RegistrationException(Exception):
    pass

class UserAlreadyExists(RegistrationException):
    pass

class RecipmentDoNotMatchCriteria(RegistrationException):
    pass

class PasswordDoNotMatchCriteria(RegistrationException):
    pass

class AddressDoNotMatchCriteria(RegistrationException):
    pass


