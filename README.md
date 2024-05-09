# Socketio Server Demo with Socket.IO

This project demonstrates a simple  socketio server using  python-socketio in Python with FastAPI and SQLAlchemy for database interaction.

## Getting Started

### Prerequisites

- Python 3.7+
- PostgreSQL
- pip (Python package manager)

### Installation

1.Create a virtual environment (optional but recommended):

```python -m venv venv```

for activate the virtual environment

```venv\Scripts\activate```

2.Install the required Python packages:
```pip install -r requirements.txt```

3.Create a .env file:

```DATABASE_URL="postgresql+asyncpg://username:password@localhost:5432/database_name"```

Note: Change username,password,port according to your database in URL

4.Create database and table

```python init_db.py```

5.Run the main server:

```python main.py```
or
```uvicorn main:app --reload```

6.Run the client:

```python client.py```
