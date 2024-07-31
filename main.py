
from fastapi import FastAPI

from .core.schemas.stores import store_curitiba, store_miami, store_santiago_chile
from .routes.companies import route_companies
from .routes.stores import route_stores, stores_list

app = FastAPI()
app.include_router(route_stores)
app.include_router(route_companies)


stores_list.extend([store_curitiba, store_santiago_chile, store_miami])


@ app.get("/", include_in_schema=False)
def index() -> dict[str, str]:
    return {"message": "Hello, World!"}
