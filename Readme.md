# Scientific Calculator with DevOps

## Overview

This project is a **Scientific Calculator** implemented in Python. It supports:

- Square root: `√x`  
- Factorial: `!x`  
- Natural logarithm (base e): `ln(x)`  
- Power function: `x^b`  

Additionally, the project demonstrates a **full DevOps pipeline** including:

- Source control with Git/GitHub  
- Unit testing with `pytest`  
- Docker containerization  
- Deployment using Ansible  

---

## Features

- Menu-driven command-line calculator  
- Fully tested with `pytest`  
- Dockerized for easy deployment  
- Ansible playbook for automated deployment  

---

## Prerequisites

- Python 3.10+  
- Git  
- Docker  
- Ansible  
- (Optional) Jenkins for CI/CD  

---

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/YOURUSERNAME/sci-calculator.git
cd sci-calculator
````

### Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the Calculator

```bash
python main.py
```

Follow the on-screen menu to select operations.

---

### Run Tests

```bash
PYTHONPATH=. pytest -v
```

---

## Docker

### Build Image

```bash
docker build -t YOURDOCKERHUBUSER/sci-calculator:1.0 .
```

### Login to Docker Hub

```bash
docker login -u YOURDOCKERHUBUSER
# Use Personal Access Token if using Google SSO
```

### Push Image

```bash
docker push YOURDOCKERHUBUSER/sci-calculator:1.0
```

---

## Deployment with Ansible

Install Docker modules for Ansible:

```bash
ansible-galaxy collection install community.docker
```

Run the playbook locally:

```bash
ansible-playbook -i ansible/inventory ansible/deploy.yml --extra-vars "image=YOURDOCKERHUBUSER/sci-calculator:1.0"
```

---

## Project Structure

```
sci-calculator/
├── ansible/
│   ├── deploy.yml
│   └── inventory
├── tests/
│   └── test_calculator.py
├── calculator.py
├── main.py
├── Dockerfile
├── requirements.txt
├── Jenkinsfile
└── README.md
```

