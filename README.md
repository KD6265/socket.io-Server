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

3.Create database and table

```python init_db.py```

Note: Change password according to your  database in  init_db

4.Run the main server:

```python main.py```
or
```uvicorn main:app --reload```

5.Run the client:

```python client.py```
