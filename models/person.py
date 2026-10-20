import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class Person:
    def __init__(self, name, email=""):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Name must be a non-empty string.")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # allow empty email
        value = value.strip() if isinstance(value, str) else ""
        if value != "" and not EMAIL_PATTERN.match(value):
            raise ValueError("Email looks invalid.")
        self._email = value

    def __str__(self):
        if self.email:
            return f"{self.name} <{self.email}>"
        return self.name
