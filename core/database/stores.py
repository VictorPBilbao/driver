from email.mime import application

import httpx

from ..schemas.stores import store_curitiba, store_miami, store_santiago_chile

# get request from 127.0.0.1:8181

DATABASE_URL = "http://127.0.0.1:8181"
PASS = "root"
USER = "root"
ACCEPT = "application/json"

# * curl example:
# curl - -location 'http://localhost:8181/signin' \
#     - -header 'Accept: application/json' \
#     - -header 'Content-Type: application/json' \
# - -data '{"user":"root","pass":"root"}'

# * making the same request using httpx

httpx.post(f"{DATABASE_URL}/signin", headers={"Accept": ACCEPT,
           "Content-Type": ACCEPT}, json={"user": USER, "pass": PASS})


def create_initial_entries():
    httpx.post(f"{DATABASE_URL}/key/Store",
               headers={"Accept": "application/json",
                        "NS": "main",
                        "DB": "main",
                        "Content-Type": "application/json"},
               auth=("root", "root"),
               json=store_curitiba.model_dump())
