
import httpx
from icecream import ic

from ..schemas.stores import store_curitiba, store_miami, store_santiago_chile
from .database_setup import *


def create_initial_entries():
    a = httpx.post(f"{DATABASE_URL}/key/Store",
                   headers={"Accept": CONTENT_TYPE,
                            "NS": "main",
                            "DB": "main",
                            "Content-Type": CONTENT_TYPE},
                   auth=(USER, PASS),
                   json=store_curitiba.model_dump())
    ic(a.json())


def read_stores():
    response = httpx.post(f"{DATABASE_URL}/sql", headers={"Accept": CONTENT_TYPE,
                                                          "NS": "main",
                                                          "DB": "main",
                                                          "Content-Type": "text/plain"},
                          auth=(USER, PASS), content=b"SELECT * FROM Store FETCH address")
    return response.json()[0]
