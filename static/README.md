# BLUE TECH – Password Analyzer

A Python-based password analyzer with a web interface built using HTML, CSS and JavaScript.

## Project Overview

BLUE TECH is a beginner cybersecurity project designed to evaluate password strength using a set of predefined security criteria.

The application analyzes a password and generates a security report containing a score, a strength level and recommendations.

## Features

- Password length verification (minimum 12 characters).
- Lowercase and uppercase letter detection.
- Digit and special character detection.
- Consecutive character repetition detection.
- Ascending sequence detection (e.g. `123`, `abc`).
- Security score calculation (0–100).
- Password strength classification:
  - Weak
  - Medium
  - Strong
- Recommendations to improve password security.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Password analysis logic |
| FastAPI | Backend API |
| Pydantic | Request data validation |
| HTML | Web page structure |
| CSS | User interface and styling |
| JavaScript | Frontend/API communication |

## Project Structure

```text
BLUE-TECH/
├── password.py
├── static/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── digital.png
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd BLUE-TECH
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python -m uvicorn password:app --reload --port 8000
```

Open the application:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## How It Works

1. The user enters a password in the web interface.
2. JavaScript sends a POST request to the FastAPI endpoint `/analyze`.
3. FastAPI validates the request using Pydantic.
4. The Python analyzer evaluates the password.
5. The API returns a JSON report.
6. JavaScript displays the score, strength level and recommendations.

## Security and Limitations

- The application is designed for local testing and educational purposes.
- Passwords are processed by the local backend.
- This project is not a professional password security auditing tool.
- The scoring system is rule-based and does not measure password entropy or check against breached-password databases.

## Future Improvements

- Add a visual security score indicator.
- Improve the password analysis algorithm.
- Add a show/hide password feature.
- Improve responsive design.
- Add automated tests.
- Improve password security recommendations.

## Project Status

**Version:** 1.0 – Initial functional prototype.

Developed as a personal learning project in cybersecurity and web development.