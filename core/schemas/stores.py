from pydantic import BaseModel, EmailStr, Field


class Address(BaseModel):
    zip_code: str
    country: str = Field(min_length=2, max_length=2)
    state: str = ""
    city: str
    street: str = ""
    number: str = ""


class PhoneLevels(BaseModel):
    name: str = ""
    purpose: str = ""
    number: str = ""


class EmailLevels(BaseModel):
    name: str = ""
    purpose: str = ""
    email: EmailStr = ""


class Contact(BaseModel):
    phone: list[PhoneLevels] = []
    emergency_phone: str = ""
    email: list[EmailLevels] = []
    website: str = ""


class Store(BaseModel):
    name: str
    IATA: str
    address: Address
    contacts: Contact = Contact()
    active: bool = True


class StoreCreate(BaseModel):
    name: str
    IATA: str
    address: Address
