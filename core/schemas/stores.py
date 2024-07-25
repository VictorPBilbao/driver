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

# Examples


store_curitiba = Store(
    name="Curitiba Airport",
    IATA="CWB",
    address=Address(
        country="BR",
        state="PR",
        city="Curitiba",
        zip_code="83010-900",
        street="Avenida Rocha Pombo",
        number="1241",
    ),
    contacts=Contact(
        phone=[
            PhoneLevels(
                name="Main",
                purpose="Contato Principal",
                number="+55 41 3381-1515"
            ),
            PhoneLevels(
                name="Informações e no-shows",
                purpose="Informações e no-shows",
                number="+55 41 3381-1515"
            )
        ],
        emergency_phone="+55 41 3381-1516",
        email=[
            EmailLevels(
                name="Main",
                purpose="Email Geral",
                email="victor.pasini@rentcars.com"
            ),
            EmailLevels(
                name="Email para no-shows",
                purpose="Email para no-shows gerais",
                email="ana.claudia@localiza.com"
            )
        ],
    )
)

store_santiago_chile = Store(
    name="Santiago Airport",
    IATA="SCL",
    address=Address(
        country="CL",
        city="Santiago",
        zip_code="8320163",
        street="Armando Cortinez Norte",
        number="2501",
    ),
    contacts=Contact(
        phone=[
            PhoneLevels(
                name="Main",
                purpose="Telefono Principal",
                number="+56 2 2690 1300"
            ),
            PhoneLevels(
                name="Information and No-Shows",
                purpose="Information contact",
                number="+56 2 2690 1301"
            )
        ],
        emergency_phone="+56 2 2690 1302",
        email=[
            EmailLevels(
                name="Main",
                purpose="Main contact",
                email="test@mail.com"
            )
        ],
    )
)

store_miami = Store(
    name="Miami Airport",
    IATA="MIA",
    address=Address(
        country="US",
        state="FL",
        city="Miami",
        zip_code="33122",
        street="N.W. 25th Street",
        number="3900",
    ),
    contacts=Contact(
        phone=[
            PhoneLevels(
                name="Main",
                purpose="Main contact",
                number="+1 305 871 2000"
            ),
            PhoneLevels(
                name="Information and No-Shows",
                purpose="Information contact",
                number="+1 305 871 2001"
            )
        ],
        emergency_phone="+1 305 871 2002"
    ),
    active=False
)
