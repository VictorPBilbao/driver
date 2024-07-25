
from surrealdb import SurrealHTTP


async def main():
    """Example of how to use the SurrealDB client."""
    async with SurrealHTTP(url="http://localhost:8181", namespace="test", database="test", username="root", password="root") as db:
        curitiba_store = {
            "name": "Curitiba Airport",
            "IATA": "CWB",
            "address": {
                "zip_code": "83010-900",
                "country": "BR",
                "state": "PR",
                "city": "Curitiba",
                "street": "Avenida Rocha Pombo",
                "number": "1241"
            },
            "contacts": {
                "phone": [
                    {
                        "name": "Main",
                        "purpose": "Contato Principal",
                        "number": "+55 41 3381-1515"
                    },
                    {
                        "name": "Informações e no-shows",
                        "purpose": "Informações e no-shows",
                        "number": "+55 41 3381-1515"
                    }
                ],
                "emergency_phone": "+55 41 3381-1516",
                "email": [
                    {
                        "name": "Main",
                        "purpose": "Email Geral",
                        "email": "victor.pasini@rentcars.com"
                    },
                    {
                        "name": "Email para no-shows",
                        "purpose": "Email para no-shows gerais",
                        "email": "ana.claudia@localiza.com"
                    }
                ],
                "website": ""
            },
            "active": True
        }

        await db.create(
            f"store:{curitiba_store["IATA"]}", curitiba_store
        )

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
