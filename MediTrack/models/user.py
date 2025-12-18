from utils.exceptions import AccessDeniedError

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def check_access(self, allowed_roles):
        if self.role not in allowed_roles:
            raise AccessDeniedError(
                f"{self.role} is not allowed to access this feature"
            )
