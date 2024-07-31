from icecream import ic

from ...core.schemas.companies import Company
from .database_setup import *


def create_company_databse(company: Company):
    ic(company.model_dump())
    return surreal_sql(f'CREATE Company:{company.slug} CONTENT {company.model_dump()}')


def get_companies_database():
    return surreal_sql("SELECT * FROM Company")
