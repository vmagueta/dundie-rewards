from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


class InvalidEmailError(Exception):
    """Invalid email error."""

    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @field_validator("pk")
    def validate_email(cls, v: str) -> str:
        if not check_valid_email(v):
            raise InvalidEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self) -> str:
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    class ConfigDict:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    actor: str
    value: Decimal
    date: datetime = Field(default_factory=lambda: datetime.now().isoformat())

    class ConfigDict:
        json_encoders = {Person: lambda p: p.pk}


class User(BaseModel):
    person: Person
    password: str = Field(default_factory=generate_simple_password)

    class ConfigDict:
        json_encoders = {Person: lambda p: p.pk}


if __name__ == "__main__":
    p = Person(pk="bruno@g.com", name="Bruno", dept="Sales", role="NA")
    print(p)
    print(p.json())

    b = Balance(person=p, value=100)
    print(b.json(models_as_dict=False))

    m = Movement(person=p, date=datetime.now(), actor="sys", value=10)
    print(m.json(models_as_dict=False))

    u = User(person=p)
    print(u.json(models_as_dict=False))

    email = "invalid@"
    try:
        Person(pk=email)
    except InvalidEmailError as e:
        assert str(e) == f"Invalid email for {email!r}"
