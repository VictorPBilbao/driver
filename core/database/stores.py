from os import getenv

import httpx
from dotenv import load_dotenv
from icecream import ic

from ..schemas.stores import store_curitiba, store_miami, store_santiago_chile

load_dotenv("../../.env")

DATABASE_URL: str | None = getenv("DATABASE_URL")
PASS: str = str(getenv("DATABASE_PASSWORD"))
USER: str = str(getenv("DATABASE_USERNAME"))
CONTENT_TYPE = "application/json"


def login() -> None:
    httpx.post(f"{DATABASE_URL}/signin", headers={"Accept": CONTENT_TYPE,
                                                  "Content-Type": CONTENT_TYPE}, json={"user": USER, "pass": PASS})


def create_initial_entries():
    httpx.post(f"{DATABASE_URL}/key/Store",
               headers={"Accept": CONTENT_TYPE,
                        "NS": "main",
                        "DB": "main",
                        "Content-Type": CONTENT_TYPE},
               auth=("root", "root"),
               json=store_curitiba.model_dump())


def read_stores():
    login()
    ic("Reading stores")
    ic(DATABASE_URL, PASS, USER)
    response = httpx.post(f"{DATABASE_URL}/sql", headers={"Accept": CONTENT_TYPE,
                                                          "NS": "main",
                                                          "DB": "main",
                                                          "Content-Type": "text/plain"},
                          auth=(USER, PASS), content=b"SELECT * FROM Store FETCH address")
    ic(response)
    ic(response.json())
    return response.json()[0]
