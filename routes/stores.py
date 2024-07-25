from math import e
from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Path, responses, status

from ..core.schemas.stores import Store, StoreCreate

route_stores = APIRouter(
    prefix="/store",
    tags=["Store Operations"],
)

stores_list: list[Store] = []


@route_stores.get("", summary="List stores", description="Get a list of all stores that match the query", response_description="A list of stores")
def get_stores(active: bool | None = None) -> list[Store]:
    if active is None:
        return stores_list
    return [store for store in stores_list if store.active == active]


@route_stores.post("", summary="Create a store", description="Create a new store", response_description="A dictionary with a success message", responses={
    status.HTTP_201_CREATED: {
        "description": "Store created successfully",
        "content": {
            "application/json": {
                "example": {
                    "message": "Store created successfully!"
                }
            }
        }
    }
}, status_code=status.HTTP_201_CREATED)
def create_store(store: Annotated[StoreCreate, Body(
    examples=[{
        "name": "Santiago Airport",
        "IATA": "SCL",
        "address": {
            "country": "CL",
            "city": "Santiago",
            "zip_code": "8320163",
            "street": "Armando Cortinez Norte",
        }
    }]
)]) -> dict[str, str]:
    store_to_create = Store(
        **store.model_dump(),
    )
    stores_list.append(store_to_create)
    return {"message": "Store created successfully!"}


@ route_stores.get("/{iata}", summary="Get a store", description="Get a store by its IATA code", response_description="The store with the specified IATA code")
def get_store(iata: Annotated[str, Path(
        description="This is the [**International Air Transport Association**](https://www.iata.org/en/services/codes/) code, that identifies each store in the system, not only in airports",
        example="SCL",
        min_length=3,
        max_length=3
)]) -> Store:
    for store in stores_list:
        if store.IATA == iata:
            return store
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Store with IATA {iata} not found")


@ route_stores.delete("/{iata}", summary="Delete a store", description="Delete a store by its IATA code", status_code=status.HTTP_204_NO_CONTENT)
def delete_store(iata: Annotated[str, Path(
    description="This is the [**International Air Transport Association**](https://www.iata.org/en/services/codes/) code, that identifies each store in the system, not only in airports",
    example="SCL",
    min_length=3,
    max_length=3
)]) -> None:
    for index, store in enumerate(stores_list):
        if store.IATA == iata:
            stores_list.pop(index)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Store with IATA {iata} not found")


@ route_stores.put("/{iata}", summary="Update a store", description="Update a store by its IATA code", response_description="A dictionary with a success message", responses={
    status.HTTP_200_OK: {
        "description": "Store updated successfully",
        "content": {
            "application/json": {
                "example": {
                    "message": "Store updated successfully"
                }
            }
        }
    }
})
def update_store(iata: Annotated[str, Path(
    description="This is the [**International Air Transport Association**](https://www.iata.org/en/services/codes/) code, that identifies each store in the system, not only in airports",
    example="SCC",
    min_length=3,
    max_length=3
)], store_updates: Annotated[StoreCreate, Body(
    examples=[{
        "name": "Santiago Airport",
        "IATA": "SCL",
        "address": {
            "country": "CL",
            "city": "Santiago",
            "zip_code": "8320163",
            "street": "Armando Cortinez Norte",
        }
    }]
)]) -> dict[str, str]:
    for index, store in enumerate(stores_list):
        if store.IATA == iata:
            stores_list[index] = Store(
                **store_updates.model_dump(),
            )
            return {"message": "Store updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Store with IATA {iata} not found")
