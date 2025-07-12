class CredentialError(Exception):
    pass

class AuthCodeMissingError(Exception):
    pass

class IncorrectAuthCodeError(Exception):
    pass

class ExpiredAuthCodeError(Exception):
    pass

class AuthCodeAlreadyUsedError(Exception):
    pass