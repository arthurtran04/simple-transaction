# Simple Transaction Application using Flask

## Introduction

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Structure

```
Basic-Math-App/
├── Maths/
│   ├── __init__.py
│   ├── mathematics.py
│   └── __pycache__/
│       ├── __init__.cpython-312.pyc
│       └── mathematics.cpython-312.pyc
├── static/
│   └── script.js
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Features

- Simple Flask web application for basic math
- Basic routing
- Basic HTML, JavaScript

## Installation

To run this project locally, open the Terminal and follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/arthurtran04/Basic-Math-App.git
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the Flask application, run the `cd` command to change the directory to `Basic-Math-App` and run the `app.py` file:

   ```bash
   cd Basic-Math-App
   python3.12 app.py
   ```
This application will run locally at `http://127.0.0.1:5000`:

<img width="600rem" alt="Screenshot 2025-04-05 lúc 01 29 30" src="https://github.com/user-attachments/assets/d33cc90b-1999-4905-aac3-690455e6a28c" />

<img width="600rem" alt="Screenshot 2025-04-05 lúc 01 32 01" src="https://github.com/user-attachments/assets/2b614832-3549-4e72-8c93-5468c182121f" />

On the webpage, there are 5 basic arithmetic operations you can try like `Add`, `Subtract`, `Multiply`, `Divide` and `Modulo`:

<img width="600rem" alt="Screenshot 2025-04-05 lúc 01 37 20" src="https://github.com/user-attachments/assets/2e95ab54-9dbb-494e-b25d-2f1dda7f5ec8" />

Additionally, you can also use different routes include `/sum`, `/sub`, `/mul`, `/div` and `/mod`.
You need to asign a value to two parameters `num1` and `num2` into the URL to calculate, example `http://127.0.0.1:5000/div?num1=2.1&num2=3.2` (`num1 = 2.1`, `num2 = 3.2`)

<img width="600rem" alt="Ảnh chụp Màn hình 2025-04-05 lúc 01 51 43" src="https://github.com/user-attachments/assets/d2b03b25-ca64-460e-bea3-c01e4dc6140b" />

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
