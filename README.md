# **Aiogram Project Template**

> A clean and well-structured template to kickstart your Telegram Bot projects efficiently. Includes modular architecture, environment setup, and clear guidelines.

---

## **Features**
- **Modular Design**: Organized code structure for scalability.
- **Environment Management**: Pre-configured `.env` example file for secure settings.
- **Dependency Management**: Powered by [Poetry](https://python-poetry.org/) for simplified package management.
- **Error Handling**: Centralized error-handling logic.
- **State Management**: FSM-ready structure for complex workflows.

---

## **Project Structure**

```plaintext
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
```

---

## **Getting Started**

### **1. Clone the Repository**
```bash
https://github.com/khurshiduktamov/aiogram-bot-template.git
cd aiogram-bot-template
```

### **2. Install Dependencies**
Ensure Poetry is installed and run:
```bash
poetry install
```

### **3. Configure Environment Variables**
- Copy `env.example` to `.env`:
```bash
cp env.example .env
```
- Add your configuration values to the `.env` file.

### **4. Run the Application**
```bash
poetry run python app/main.py
```

---

## **Contributing**
We welcome your contributions! Please:
1. Fork the repository.
2. Create a branch for your changes.
3. Submit a pull request for review.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
- **Author**: Khurshid Uktamov
- **Email**: [xurshid3777@gmail.com](mailto:xurshid3777@gmail.com)
- **GitHub**: [https://github.com/khurshiduktamov](https://github.com/khurshiduktamov)

---
