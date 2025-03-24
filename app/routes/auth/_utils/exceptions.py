class UserAccountCreationCheckExcetiption(Exception):
    def __init__(self, data: dict, message: str):
        self.data = data
        self.message = message