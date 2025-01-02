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
│   ├── main.py                # Entry point for the project
│   ├── config.py              # Configuration settings
│   ├── errors/
│   │   ├── __init__.py
│   │   ├── error_handler.py   # Centralized error handling
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── users.py           # User-specific logic
│   │   ├── groups.py          # Group-specific logic
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── keyboards.py       # Inline and reply keyboards
│   │   ├── menus.py           # Menu-based keyboards
│   ├── states/
│   │   ├── __init__.py
│   │   ├── registration.py    # FSM states for workflows
│
│env.example                   # Environment variable template
│poetry.lock                   # Locked dependencies for consistency
│pyproject.toml                # Project dependencies and settings
```

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-project-template.git
cd your-project-template
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

## **Why Include `poetry.lock`?**

The `poetry.lock` file ensures:
- **Consistency**: Same versions of dependencies for all developers and environments.
- **Reproducibility**: Avoids unexpected issues caused by updated dependencies.
- **Stability**: Reduces deployment risks in production.

### When to Exclude It:
If you're creating a library for others to install, omit the `poetry.lock` file since users will resolve their own dependencies.

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
- **Author**: [Khurshid Uktamov]
- **Email**: [xurshid3777@gmail.com](mailto:xurshid3777@gmail.com)
- **GitHub**: [https://github.com/khurshiduktamov](https://github.com/khurshiduktamov)

---
