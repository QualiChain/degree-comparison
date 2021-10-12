import requests

url = 'http://127.0.0.1:5000/compare/similarity'  # localhost and the defined port + endpoint
params = {
    'file1_path': 'test_file1.json',
    'file2_path': 'test_file2.json',
}
response = requests.get(url, params=params)
print(response.url)

"""
http://10.116.60.96:5000/compare/similarity?file1_path=ist-legi.json&file2_path=ist-leic.json
http://127.0.0.1:1080/compare/similarity?file1_path=test_file1.json&file2_path=test_file2.json
http://127.0.0.1:1080/compare/ects?file1_path=test_file1.json&file2_path=test_file2.json
http://127.0.0.1:1080/compare/ects?file1_path=ist-legi.json&file2_path=ist-leic.json
 http://172.17.0.2:5000/compare/similarity?file1_path=ist-legi.json&file2_path=ist-leic.json
http://localhost:5000/compare/similarity?file1_path=ist-legi.json&file2_path=ist-leic.json
 
"""

