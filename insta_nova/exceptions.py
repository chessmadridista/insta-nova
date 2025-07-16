class CredentialTypeError(TypeError):
    pass

class CredentialValueError(ValueError):
    pass

class AuthCodeMissingError(Exception):
    pass

class IncorrectAuthCodeError(Exception):
    pass

class ExpiredAuthCodeError(Exception):
    pass

class AuthCodeAlreadyUsedError(Exception):
    pass

class EmptyAuthCodeError(Exception):
    pass

class AuthorizationCodeTypeError(Exception):
    pass

class RedirectUriTypeError(Exception):
    pass

class InstagramUserIdTypeError(Exception):
    pass
