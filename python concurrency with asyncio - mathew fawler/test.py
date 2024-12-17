import http.client

conn = http.client.HTTPSConnection("127.0.0.1", 8000)

headersList = {
 "Content-Type": "text/plain" 
}

payload = "salam"

conn.request("GET", "/", payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))