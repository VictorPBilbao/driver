from os import getenv

import httpx
from dotenv import load_dotenv

load_dotenv("../../.env")

DATABASE_URL: str | None = getenv("DATABASE_URL")
PASS: str = str(getenv("DATABASE_PASSWORD"))
USER: str = str(getenv("DATABASE_USERNAME"))
CONTENT_TYPE = "application/json"


def surreal_sql(query: str) -> list[dict]:
    print(query)
    return httpx.post(f"{DATABASE_URL}/sql", headers={"Accept": CONTENT_TYPE,
                                                      "NS": "main",
                                                      "DB": "main",
                                                      "Content-Type": "text/plain"},
                      auth=(USER, PASS), content=query).json()


def set_items_from_model(model, exclude: set = set()) -> str:
    return ", ".join([f"{k}='{v}'" for k, v in model.model_dump(exclude=exclude).items()])
