from operator import ge

from fastapi import APIRouter

from ..core.database.companies import create_company_databse, get_companies_database
from ..core.schemas.companies import Company, localiza, ready_ar

route_companies = APIRouter(
    prefix="/company",
    tags=["Company Operations"],
)


@route_companies.get("")
def get_companies():
    return get_companies_database()


@route_companies.post("")
def create_company(company: Company):
    return create_company_databse(company)
