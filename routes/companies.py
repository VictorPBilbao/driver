from fastapi import APIRouter

from ..core.database.companies import (
    create_company_database,
    delete_company_by_slug_database,
    get_companies_database,
    get_company_by_slug_database,
    insert_multiple_companies_database,
    update_company_by_slug_database,
)
from ..core.schemas.companies import Company, test_companies

route_companies = APIRouter(
    prefix="/company",
    tags=["Company Operations"],
)


@route_companies.get("")
def get_all_companies() -> list[dict]:
    return get_companies_database()


@route_companies.get("/start")
def populate_companies() -> list[dict]:
    return insert_multiple_companies_database([company.model_dump(by_alias=True) for company in test_companies])


@route_companies.get("/{slug}")
def get_company_by_slug(slug: str) -> list[dict]:
    return get_company_by_slug_database(slug)


@route_companies.post("")
def create_company(company: Company) -> list[dict]:
    return create_company_database(company)


@route_companies.delete("/{slug}")
def delete_company(slug: str) -> list[dict]:
    return delete_company_by_slug_database(slug)


@route_companies.put("/{slug}")
def update_company(slug: str, company: Company) -> list[dict]:
    return update_company_by_slug_database(slug, company)
