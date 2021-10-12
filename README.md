# degree-comparison

The Degree Comparison component defined in task T4.2.

For now it includes:
- a schema that defines the format of the degrees to be compared (degree.schema.json)
- a very simple example, not a full degree, just to help understand the schema (simple-example.json)
- the definition of a set of real IST degrees (ist*.json)

The real degrees can be compared among themselves. A quick inspection shows that some are related, whereas others are not.

# Degree Comparision
python app.py

# REST ENDPOINT for Course comparison
http://127.0.0.1:1080/compare/similarity

Example for sending a request using curl:
curl -i -X GET -F file1_path=@ist-legi.json -F file2_path=@ist-leic.json "http://localhost:5000/compare/similarity"

# REST endpoint for ECTS comparison
http://127.0.0.1:1080/compare/ects
