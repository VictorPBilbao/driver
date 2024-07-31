from pydantic import BaseModel


class Company(BaseModel):
    slug: str
    name: str


localiza: dict[str, str] = {
    "slug": "localiza",
    "name": "Localiza"
}

ready_ar: dict[str, str] = {
    "slug": "ready_ar",
    "name": "Ready Argentina"
}
