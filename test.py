out_keys = ["course1","course2","similarity"]

out_dict = {out_key: None for out_key in out_keys}

output = {"1": {}}

# print(output)

out_dict['course1'] = "Maths"
out_dict['course2'] = "science"
out_dict['similarity'] = "0.53"

output["1"] = out_dict

out_dict['course1'] = "Maths"
out_dict['course2'] = "science"
out_dict['similarity'] = "0.53"

output["2"] = out_dict

print(output)