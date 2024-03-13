import requests
import base64

# Define the URL
url = "https://wso2-api-gateway-direct-kcb-wso2-gateway.apps.test.aro.kcbgroup.com/token"

# Define the credentials
username = "AndrexxCodes"
password = "GPk@yniYUic8@HT"
consumer_key = "8yAVcwI0AaTQRB72PhDDTcNXecsa"
consumer_secret = "QsvvuUIO2DLmPVmsR9S6yroN2u0a"

# Encode consumer key and secret to Base64
credentials = f"{consumer_key}:{consumer_secret}"
credentials_b64 = base64.b64encode(credentials.encode()).decode()

# Define the payload
payload = {
    "grant_type": "password",
    "username": username,
    "password": password
}

# Define the headers
headers = {
    "Authorization": f"Basic {credentials_b64}"
}

# Make the POST request
response = requests.post(url, data=payload, headers=headers, verify=False)

# Print the response
print(response.json())
