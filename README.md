> [!NOTE]
> **This project is currently in active development. Any contributions, feedback, or help are warmly welcome!**

# RefactorAI

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]

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
refactorai file.py
```

### **Refactor a directory:**

**Current directory**

```bash
refactorai
```

**Any directory**

```bash
refactorai /path/to/directory
```

**Recursively**

> [!WARNING]
> Make sure the directory has no venv in it.

```bash
refactorai /path/to/directory -r
```

---

## 👷‍♀️ Contributing 👷

Please contribute to this project by submitting **Issues** or **PR's**.
Thank you for your interest in _RefactorAI_.


[contributors-shield]: https://img.shields.io/github/contributors/nikolaspoczekaj/RefactorAI.svg?style=for-the-badge
[contributors-url]: https://github.com/nikolaspoczekaj/RefactorAI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nikolaspoczekaj/RefactorAI.svg?style=for-the-badge
[forks-url]: https://github.com/nikolaspoczekaj/RefactorAI/network/members
[stars-shield]: https://img.shields.io/github/stars/nikolaspoczekaj/RefactorAI.svg?style=for-the-badge
[stars-url]: https://github.com/nikolaspoczekaj/RefactorAI/stargazers
[issues-shield]: https://img.shields.io/github/issues/nikolaspoczekaj/RefactorAI.svg?style=for-the-badge
[issues-url]: https://github.com/nikolaspoczekaj/RefactorAI/issues
[license-shield]: https://img.shields.io/github/license/nikolaspoczekaj/RefactorAI.svg?style=for-the-badge
[license-url]: https://github.com/nikolaspoczekaj/RefactorAI/blob/master/LICENSE.txt
