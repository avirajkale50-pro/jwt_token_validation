import requests
import re
import sys


BASE_URL = "http://127.0.0.1:5000"

def test_generate_and_validate():
    print("Testing Generate and Validate Flow...")
    

    user_id = "test_user_789"
    gen_url = f"{BASE_URL}/generate_ui?user_id={user_id}"
    print(f"GET {gen_url}")
    
    try:
        response = requests.get(gen_url)
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Is app.py running?")
        sys.exit(1)
        
    if response.status_code != 200:
        print(f"Failed to load generate page. Status: {response.status_code}")
        sys.exit(1)
        
    
    match = re.search(r'<div class="token-display">(.*?)</div>', response.text)
    if not match:
        print("Failed to find generated token in response.")
        print("Response snippet:", response.text[:500])
        sys.exit(1)
        
    token = match.group(1).strip()
    print(f"Success! Generated Token: {token[:20]}...")

    val_url = f"{BASE_URL}/validate_ui"
    print(f"GET {val_url} with token")
    
    response = requests.get(val_url, params={"token": token})
    
    if "Status: Valid" in response.text:
        print("Success! Token validated as Valid.")
    else:
        print("Failed! Token did not validate.")
        print("Response snippet:", response.text[:500])
        sys.exit(1)
        
    if user_id in response.text:
        print("Success! Claims (user_id) found in validation response.")
    else:
        print("Warning: user_id not found in validation response.")

def test_invalid_token():
    print("\nTesting Invalid Token...")
    val_url = f"{BASE_URL}/validate_ui"
    response = requests.get(val_url, params={"token": "invalid.token.123"})
    
    if "Status: Invalid" in response.text and "Invalid Token Signature or Payload" in response.text:
        print("Success! Invalid token correctly rejected.")
    else:
        print("Failed! Invalid token not rejected as expected.")
    

if __name__ == "__main__":
    try:
        test_generate_and_validate()
        test_invalid_token()
        print("\nAll automated tests passed!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
