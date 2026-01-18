from flask import Flask, request, render_template
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = "mysecret123"

@app.route("/generate")
def generate_token():
    user_id = request.args.get("user_id", "123")

    payload = {
        "sub": user_id,
        "role": "user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token


@app.route("/validate")
def validate_token():
    token = request.args.get("token")

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return f"Token Valid: {decoded}"

    except jwt.ExpiredSignatureError:
        return "Token Invalid: Token Expired"

    except jwt.InvalidTokenError:
        return "Token Invalid"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_ui")
def generate_ui():
    user_id = request.args.get("user_id")

    if not user_id:
        user_id = "123"

    payload = {
        "sub": user_id,
        "role": "user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return render_template("index.html", generated_token=token, user_id=user_id)


@app.route("/validate_ui")
def validate_ui():
    token = request.args.get("token")
    
    if not token:
        return render_template("index.html", validation_error="No token provided")

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return render_template("index.html", validation_result="Valid", claims=decoded, Token=token)

    except jwt.ExpiredSignatureError:
        return render_template("index.html", validation_result="Invalid", validation_error="Token Expired", Token=token)

    except jwt.InvalidTokenError:
        return render_template("index.html", validation_result="Invalid", validation_error="Invalid Token Signature or Payload", Token=token)



if __name__ == "__main__":
    app.run(debug=True)

