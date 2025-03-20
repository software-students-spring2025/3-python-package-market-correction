# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Developer Setup Guide for procrastination\_helper

Follow these steps to set up and contribute to the **procrastination\_helper** project:

### 1. Clone the Repository

```bash
git clone https://github.com/software-students-spring2025/3-python-package-market-correction.git
cd 3-python-package-market-correction
```

### 2. Set Up a Virtual Environment

You can use either `venv` or `pipenv`:

- **Using venv:**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

- **Using pipenv:**

```bash
pipenv shell
```

### 3. Install Dependencies

- **Using venv:**

```bash
pip install -e .[dev]
```

- **Using pipenv:**

```bash
pipenv install -e .[dev]
```

### 4. Run Tests

Ensure everything is working by running:

```bash
pytest
```

### 5. Build the Package

To package the application, use:

```bash
python -m build
```

### 6. Run the Application

Navigate to the source directory and execute:

```bash
cd src
python3 -m procrastination_helper
```

### Platform Compatibility

This project is compatible with Windows, macOS, and Linux, requiring **Python 3.7+**.

