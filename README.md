# RefactorAI

🔁🤖**Automated Code Refactoring with AI**

RefactorAI is a CLI tool that **automatically refactors your Python code** using AI, ensuring compliance with **PEP 8**, best practices, and clean code principles. Whether you need to refactor a single file or an entire project, RefactorAI optimizes your codebase with minimal effort.

---

## ✨ **Features**

✅ **PEP 8 Compliance** – Fixes indentation, naming conventions, line length, and more.
✅ **Type Hinting & Docstrings** – Adds missing type hints and documentation.  
✅ **Unused Code Detection** – Removes unused imports, variables, and functions.  
✅ **Project-Wide Refactoring** – Processes entire directories recursively.  
✅ **Custom Instructions** – Apply project-specific refactoring rules.

---

## 🚀 **Installation**

### **Option 1: Install via pip**

```bash
pip install refactorai
```

### **Option 2: From source**

```bash
git clone https://github.com/nikolaspoczekaj/RefactorAI.git
cd RefactorAI
pip install -e .
```

---

## 🛠 Setup

### **Step 1 (optional): Setup AI Api-Key and URL as environment-variables**

You dont have to set these. But if you dont, you are promted to input them every time.

**Linux**:

```bash
export REFACTORAI_API_KEY = sk-xxxxxxxxxxxxxx
export REFACTORAI_API_URL = https://api.deepseek.com
```

**Windows**:

Set env-variables via system control.

---

## 💻 Usage

### **Refactor a single file:**

```bash
refactorai run -d /path/to/file.py
```

---

## 👷‍♀️ Contributing 👷

Please contribute to this project by submitting **Issues** or **PR's**.
Thank you for your interest in _RefactorAI_.
