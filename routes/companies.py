from fastapi import APIRouter

from ..core.database.companies import (
    create_company_databse,
    delete_company_by_slug,
    fetch_company_by_slug,
    get_companies_database,
    insert_multiple_companies,
    update_company_by_slug,
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
    return insert_multiple_companies([company.model_dump(by_alias=True) for company in test_companies])


@route_companies.get("/{slug}")
def get_company_by_slug(slug: str) -> list[dict]:
    return fetch_company_by_slug(slug)


@route_companies.post("")
def create_company(company: Company) -> list[dict]:
    return create_company_databse(company)


@route_companies.delete("/{slug}")
def delete_company_by_slug(slug: str) -> list[dict]:
    return delete_company_by_slug(slug)


@route_companies.put("/{slug}")
def update_company_by_slug(slug: str, company: Company) -> list[dict]:
    return update_company_by_slug(slug, company)
