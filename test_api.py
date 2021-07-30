import requests

url = 'http://127.0.0.1:1080/compare/similarity'  # localhost and the defined port + endpoint
params = {
    'file1_path': 'test_file1.json',
    'file2_path': 'test_file2.json',
}
response = requests.get(url, params=params)
print(response.json)

"""
http://127.0.0.1:1080/compare/similarity?file1_path=ist-legi.json&file2_path=ist-leic.json
http://127.0.0.1:1080/compare/similarity?file1_path=test_file1.json&file2_path=test_file2.json
http://127.0.0.1:1080/compare/ects?file1_path=test_file1.json&file2_path=test_file2.json
http://127.0.0.1:1080/compare/ects?file1_path=ist-legi.json&file2_path=ist-leic.json
"""

