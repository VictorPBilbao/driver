from fastapi import HTTPException, status

from ...core.schemas.companies import Company
from .database_setup import *


def create_company_database(company: Company):
    return surreal_sql(f'CREATE Company:{company.slug} CONTENT {company.model_dump(exclude={"slug"})}')


def get_companies_database() -> list[dict]:
    return surreal_sql("SELECT * FROM Company")


def get_company_by_slug_database(slug: str) -> list[dict]:
    print(f"SELECT * FROM Company:{slug}")
    return surreal_sql(f"SELECT * FROM Company:{slug}")


def insert_multiple_companies_database(companies: list[dict]) -> list[dict]:
    return surreal_sql(f"INSERT INTO Company {companies}")


def delete_company_by_slug_database(slug: str) -> list[dict]:
    return surreal_sql(f"DELETE Company:{slug}")


def update_company_by_slug_database(slug: str, company: Company) -> list[dict] | dict:
    def slug_not_in_databse(slug: str) -> bool:
        return f"Company:{slug}" not in {company["id"] for company in surreal_sql("SELECT id FROM Company")[0]["result"]}

    if slug_not_in_databse(slug):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    else:
        return surreal_sql(f"UPDATE Company:{slug} SET {set_items_from_model(company, exclude={'slug'})}")
