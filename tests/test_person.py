from models.person import Person
import pytest

def test_person_name_setter():
    p = Person("Leslie")
    assert p.name == "Leslie"

def test_person_name_invalid():
    with pytest.raises(ValueError):
        Person("")

def test_person_email_valid():
    p = Person("Leslie", "leslie@example.com")
    assert p.email == "leslie@example.com"

def test_person_email_invalid():
    with pytest.raises(ValueError):
        Person("Leslie", "not-an-email")
