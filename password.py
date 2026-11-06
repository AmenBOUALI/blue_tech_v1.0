from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class PasswordRequest(BaseModel):
    password: str


@app.post("/analyze")
def analyze(request: PasswordRequest):
    return analyze_password(request.password)

@app.get("/")
def home():
    return FileResponse("static/index.html")
    
def check_length(password):
    return len(password) >= 12


def check_characters(password):
    lowercase = any(char.islower() for char in password)
    uppercase = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(not char.isalnum() for char in password)

    return lowercase, uppercase, digit, special


def check_repetition(password):
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    return False


def check_sequences(password):
    for i in range(len(password) - 2):
        a, b, c = password[i:i+3]

        if (ord(b) == ord(a) + 1 and
                ord(c) == ord(b) + 1):
            return True

    return False


def analyze_password(password):

    length = check_length(password)
    lowercase, uppercase, digit, special = check_characters(password)
    repetition = check_repetition(password)
    sequences = check_sequences(password)

    score = 0

    criteria = [
        (length, 25),
        (lowercase, 10),
        (uppercase, 10),
        (digit, 15),
        (special, 15),
        (not repetition, 10),
        (not sequences, 15)
    ]

    for condition, points in criteria:
        if condition:
            score += points

    if score >= 80:
        level = "Strong"
    elif score >= 50:
        level = "Medium"
    else:
        level = "Weak"

    recommendations = []

    if not length:
        recommendations.append(
            "Increase your password length to at least 12 characters."
        )

    if not lowercase:
        recommendations.append("Add lowercase letters.")

    if not uppercase:
        recommendations.append("Add uppercase letters.")

    if not digit:
        recommendations.append("Add numbers.")

    if not special:
        recommendations.append("Add special characters.")

    if repetition:
        recommendations.append(
            "Avoid consecutive repeated characters."
        )

    if sequences:
        recommendations.append(
            "Avoid predictable sequences such as 123 or abc."
        )

    return {
        "score": score,
        "level": level,
        "recommendations": recommendations
    }


def main():
    password = input("Enter your password: ")

    report = analyze_password(password)

    print("\n===== PASSWORD SECURITY REPORT =====")
    print("Security Score:", report["score"], "/100")
    print("Level:", report["level"])

    print("\nRecommendations:")

    if report["recommendations"]:
        for recommendation in report["recommendations"]:
            print("[!] ", recommendation)
    else:
        print("No basic weaknesses detected.")


if __name__ == "__main__":
    main()
