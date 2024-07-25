# Rental Company Driver API

The Rental Company Driver API is a comprehensive solution designed for rental companies to manage their operations efficiently and publish their rates through an open API. This enables Online Travel Agencies (OTAs) and other travel brokers to easily access and consume the information. The API is built using FastAPI, offering high performance and easy scalability.

## Features

- Store Management: Allows rental companies to manage their store information, including creating new stores and retrieving details of existing stores.
- Rate Publishing: Enables rental companies to publish their rental rates, making them accessible to OTAs and travel brokers.
- Query Stores: Supports querying stores based on specific criteria, such as active status.
- Open API: Provides an open API for OTAs and travel brokers to consume the published rates and store information.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/VictorPBilbao/driver.git
```

2. Navigate to the project directory:
```bash
cd driver
```

3. **[OPTIONAL]** Create a virtual environment:
```bash
python -m venv venv
```

and activate it:
```bash
venv\Scripts\activate
```

4. **[OPTIONAL]** Upgrade pip:
```bash
python -m pip install --upgrade pip
```

5. Install the project dependencies:
```bash
pip install -r requirements.txt
```

6. Start the FastAPI server:
```bash
fastapi dev main.py
```

7. Access the API documentation at your [localhost](http://127.0.0.1:8000)

8. **[OPTIONAL]** Open the API documentation in your browser:
- Swagger UI: `/docs`
- ReDoc: `/redoc`