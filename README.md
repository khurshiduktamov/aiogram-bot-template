├── app/
│   ├── __init__.py
│   ├── main.py                # Entry point
│   ├── config.py              # Bot configurations (e.g., tokens)
│   ├── errors/
│   │   ├── __init__.py
│   │   ├── error_handler.py   # Error handler
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── users.py           # Handles user-specific actions
│   │   ├── groups.py          # Handles group-specific actions
│   │   ├── channels.py        # Handles channel-specific actions
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── keyboards.py 
│   │   ├── menus.py           # Inline and reply keyboards
│   ├── states/
│   │   ├── __init__.py
│   │   ├── registration.py    # FSM states for registration
│
│env.example                   # Create .env file and copy the env.example file
│
│poetry.lock                   # venv dependencies
│pyproject.toml                # venv dependencies