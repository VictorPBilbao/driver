from pydantic import BaseModel, Field, field_validator


class Company(BaseModel):
    slug: str = Field(min_length=3, max_length=20, alias="id")
    name: str

    @field_validator("slug")
    def validate_slug(cls, value: str) -> str:
        return value.lower().replace(" ", "_")

    class Config:
        populate_by_name = True


localiza: dict[str, str] = {
    "slug": "localiza",
    "name": "Localiza"
}

ready_ar: dict[str, str] = {
    "slug": "ready_ar",
    "name": "Ready Argentina"
}

movida: dict[str, str] = {
    "slug": "movida",
    "name": "Movida Aluguel de Carros"
}

avis: dict[str, str] = {
    "slug": "avis rent a car",
    "name": "Avis"
}

ssur: dict[str, str] = {
    "slug": "ssur",
    "name": "Salfa Sur"
}

test_companies: list[Company] = [Company(**localiza), Company(**ready_ar),
                                 Company(**movida), Company(**avis), Company(**ssur)]
