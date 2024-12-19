# alpaca-py Environment Setup

A walkthrough for setting up the environment for alpaca-py.

---

## 1. Create and Activate a Python Virtual Environment

### **Step 1: Create a Virtual Environment**
To create a virtual environment for alpaca-py, navigate to your home directory or the directory where you manage virtual environments, and run:

```bash
python3 -m venv <your_virtualenv_name>
```

Ensure you deactivate any active Conda environment to avoid conflicts. Use the following command:

```bash
conda deactivate
```

### **Step 2: Activate the Virtual Environment**
Once the virtual environment is created, activate it:

```bash
source <your_virtualenv_name>/bin/activate
```

---

## 2. Install Required Packages

### **Step 1: Update `pip`**
Before installing the required packages, ensure `pip` is up-to-date:

```bash
pip install --upgrade pip
```

### **Step 2: Install Dependencies**
Navigate to the base directory of this GitHub repository and install the required packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file will handle the versions of all necessary dependencies.

