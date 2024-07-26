import httpx

from ..schemas.stores import store_curitiba, store_miami, store_santiago_chile

# get request from 127.0.0.1:8181

DATABASE_URL = "http://127.0.0.1:8181"
PASS = "root"
USER = "root"
CONTENT_TYPE = "application/json"

# * curl example:
# curl - -location 'http://localhost:8181/signin' \
#     - -header 'Accept: application/json' \
#     - -header 'Content-Type: application/json' \
# - -data '{"user":"root","pass":"root"}'

# * making the same request using httpx

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

    # curl example
    # curl - -location 'http://127.0.0.1:8181/sql' \
    #     - -header 'Accept: application/json' \
    #     - -header 'NS: main' \
    #     - -header 'DB: main' \
    #     - -header 'Content-Type: text/plain' \
    #     - -header 'Authorization: Basic cm9vdDpyb290' \
    #     - -data 'SELECT * FROM Store FETCH address'

    # making the same request using httpx

    response = httpx.post(f"{DATABASE_URL}/sql", headers={"Accept": CONTENT_TYPE,
                                                          "NS": "main",
                                                          "DB": "main",
                                                          "Content-Type": "text/plain"},
                          auth=("root", "root"), content=b"SELECT * FROM Store FETCH address")

    return response.json()[0]
