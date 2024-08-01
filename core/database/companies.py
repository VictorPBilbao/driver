from icecream import ic

from ...core.schemas.companies import Company
from .database_setup import *


def create_company_databse(company: Company):
    return surreal_sql(f'CREATE Company:{company.slug} CONTENT {company.model_dump(exclude={"slug"})}')


def get_companies_database() -> list[dict]:
    return surreal_sql("SELECT * FROM Company")


def fetch_company_by_slug(slug: str) -> list[dict]:
    print(f"SELECT * FROM Company:{slug}")
    return surreal_sql(f"SELECT * FROM Company:{slug}")


def insert_multiple_companies(companies: list[dict]) -> list[dict]:
    return surreal_sql(f"INSERT INTO Company {companies}")


def delete_company_by_slug(slug: str) -> list[dict]:
    return surreal_sql(f"DELETE Company:{slug}")


def update_company_by_slug(slug: str, company: Company) -> list[dict]:
    print(f"UPDATE Company:{slug} SET {set_items_from_model(company, exclude={'slug'})}")
    return surreal_sql(f"UPDATE Company:{slug} SET {set_items_from_model(company, exclude={'slug'})}")
