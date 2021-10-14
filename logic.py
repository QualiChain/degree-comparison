import json
from sentence_transformers import SentenceTransformer, util


class Filereader:
    file1_data = {}
    degree_name = ""
    sc_name = ""
    ects = ""
    courses = []

    def __init__(self, file1):
        #with open(file1_path, encoding="utf8") as f:
        #self.file1_data = json.dumps(file1)
        print("type of file:", type(file1))
        # file2_json = file2_byte_content.decode('utf8').replace("'", '"')
        # file1_str = "r" + file1
        self.file1_data = json.loads(file1)

        print("type of file:", type(self.file1_data))
        print(self.file1_data["properties"]["name"])

    def set_fields(self):
        self.degree_name = self.file1_data["properties"]["name"]
        self.sc_name = self.file1_data["properties"]["school"]
        self.ects = self.file1_data["properties"]["ects"]
        self.courses = self.file1_data["properties"]["courses"]

    def print(self):
        print("degree_name:", self.degree_name)
        print("courses in this degree:", self.courses)
        print("first course:", self.courses[0]['name'])
        print("first course:", self.courses[0]['ects'])

    def unset_fields(self):
        self.degree_name = ""
        self.sc_name = ""
        self.ects = ""
        self.courses = []


class DegreeComparision:
    course1_list = []
    course2_list = []
    course1_desc = []
    course2_desc = []
    ects1 = 0.0
    ects2 = 0.0
    threshold = 0.0
    output = []

    def __init__(self, course1, course2, th):
        self.course1_list = course1
        self.course2_list = course2
        self.threshold = th

    def compare_ects(self, ects1, ects2):
        result = ""
        if ects1 == ects2:
            result = "Both the Degrees have the same ECTS"
        else:
            result = "ECTS are not similar"

        return result

    def extract_description_of_courses(self):
        for i in range(len(self.course1_list)):
            self.course1_desc.append(self.course1_list[i]['description'])

        for i in range(len(self.course2_list)):
            self.course2_desc.append(self.course2_list[i]['description'])

    def calculate_similarity(self):

        # output = []

        model = SentenceTransformer('paraphrase-MiniLM-L12-v2')

        # Compute embedding for both lists
        embeddings1 = model.encode(self.course1_desc, convert_to_tensor=True)
        embeddings2 = model.encode(self.course2_desc, convert_to_tensor=True)

        # Compute cosine-similarity
        cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

        # Output the pairs with their score
        for i in range(len(self.course1_desc)):
            for j in range(len(self.course2_desc)):
                if cosine_scores[i][j] >= 0.65:
                    res_tuple = (self.course1_desc[i],
                             self.course2_desc[j],
                             cosine_scores[i][j].item())
                    self.output.append(res_tuple)

        return self.output

    def unset_fields(self):
        self.course1_desc.clear()
        self.course2_desc.clear()
        self.output.clear()


# if __name__ == '__main__':
#     file1 = Filereader("test_file1.json")
#     file1.set_fields()
#     file2 = Filereader("test_file2.json")
#     file2.set_fields()
#
#     dc = DegreeComparision(file1.courses, file2.courses, 0.5)
#     dc.extract_description_of_courses()
#
#     ects_compare_res = dc.compare_ects(file1.ects, file2.ects)
#
#     similarity_cal_res = dc.calculate_similarity()
#
#     print(similarity_cal_res)

