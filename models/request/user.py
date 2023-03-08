from pydantic import BaseModel


class RegisterUser(BaseModel):

    first_name: str
    last_name: str
    email: str
    password: str
