import requests
import curlify

url = 'http://127.0.0.1:5000/compare/similarity'
test_files = {
    "file1_path": open("ist-legi.json", "rb"),
    "file2_path": open("ist-leic.json", "rb")
}

response = requests.get(url, files=test_files)
print(response)
print(response.json())

# print(curlify.to_curl(response.request))
