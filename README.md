# JWT Authentication System

A simple, secure, and modern Flask-based application for generating and validating JSON Web Tokens (JWT). This project demonstrates the core concepts of JWT authentication including signing, claims, expiration handling, and validation.


## Setup & Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd jwt_auth_system
    ```

2.  **Set up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3.  **Install Dependencies**:
    ```bash
    pip install flask pyjwt requests
    ```

## Running the Application

1.  Start the Flask server:
    ```bash
    python3 app.py
    ```
2.  Open your browser and navigate to:
    `http://127.0.0.1:5000`

## Usage

1.  **Generate**: Enter a User ID in the "Generate JWT" section and click the button. Copy the generated token.
2.  **Validate**: Paste the token into the "Validate JWT" section and click "Validate Token".
    -   **Valid**: Shows "Status: Valid" and displays the JSON claims.
    -   **Invalid/Expired**: Shows "Status: Invalid" and the reason.

## Testing

An automated test script is included to verify the full flow (generation -> validation -> invalid token handling).

```bash
python3 test_jwt_flow.py
```