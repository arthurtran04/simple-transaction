# Simple Transaction Application using Flask

## Introduction

The **Simple Transaction App** is a lightweight application built using Flask, featuring a clean HTML-based interface. This project serves as a straightforward platform for managing transactions, combining 60.5% HTML for the front-end and 39.5% Python for the back-end functionality.

## Table of Contents

- [Introduction](#introduction)
- [Prequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequirements

- ![Python 3.7](https://img.shields.io/badge/Python-3.7-blue) or above: [Download here](https://www.python.org/downloads)

## Project Structure

```
Simple-Transaction-App/
├── .gitignore
├── templates/
│   ├── edit.html
│   ├── form.html
│   ├── search.html
│   └── transactions.html
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Features

- Simple transaction application with Flask
- Basic routing
- Basic HTML, JavaScript and Bootstrap

## Installation

To install this project, open your Terminal and follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/arthurtran04/Simple-Transaction-App.git
    ```

2. Run the `cd` command to change the directory to `Simple-Transaction-App`:

    ```bash
    cd ./Simple-Transaction-App
    ```
    
4. Create a Python virtual environment `venv` and install the required dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

To start the Flask application, run the `app.py` file:

   ```bash
   python app.py
   ```
This application will run locally at `http://127.0.0.1:5000`:

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/db277f46-ce27-4e43-b608-78608aa9876c" />

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/e09c9aab-d7e0-4fcc-b853-882c553ec6a1" />

On the webpage, there are **three** features you can try like `Add Transaction`, `Edit` and `Delete`:

1. Add:</br>
    <img width="600rem" alt="Add" src="https://github.com/user-attachments/assets/a7ead3dc-9553-486d-9aba-e7f650c309cb" />
2. Edit:</br>
    <img width="600rem" alt="Edit" src="https://github.com/user-attachments/assets/8f73e472-7175-4116-bd49-3c9fef2cdbda" />
3. Delete:</br>
    <img width="600rem" alt="Delete" src="https://github.com/user-attachments/assets/757fa2f5-9eb4-4664-89cb-423fdccfd1f5" />

Additionally, you can also use different routes, including `/search` and `/balance`.

4. Search:</br>
    <img width="600rem" alt="Search" src="https://github.com/user-attachments/assets/b81a28c2-e35b-41c9-a547-94da554654ea" />
5. Balance:</br>
    <img width="600rem" alt="Balance" src="https://github.com/user-attachments/assets/16ca1e25-75cb-4169-8ca6-d644c194d9cb" />

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
