# app.py
from flask import Flask
from flask_restful import Api, Resource, reqparse
import logic
import json
from flask import request

APP = Flask(__name__)
API = Api(APP)


class CompareECTS(Resource):

    @staticmethod
    def get():
        files = request.files
        file1 = files['file1_path']
        file1_byte_content = file1.read()
        data = json.loads(file1_byte_content)
        file1_data = json.dumps(data, indent=4, sort_keys=True)

        file2 = files['file2_path']
        file2_byte_content = file2.read()

        data2 = json.loads(file2_byte_content)
        file2_data = json.dumps(data2, indent=4, sort_keys=True)

        file1 = logic.Filereader(file1_data)
        file1.unset_fields()
        file1.set_fields()
        file2 = logic.Filereader(file2_data)
        file2.unset_fields()
        file2.set_fields()

        dc = logic.DegreeComparision(file1.courses, file2.courses, 0.7)
        dc.extract_description_of_courses()

        ects_compare_res = dc.compare_ects(file1.ects, file2.ects)

        out = json.dumps(ects_compare_res)
        return out, 200


class CompareCourses(Resource):

    @staticmethod
    def get():
        files = request.files
        file1 = files['file1_path']
        file1_byte_content = file1.read()
        data = json.loads(file1_byte_content)
        file1_data = json.dumps(data, indent=4, sort_keys=True)

        file2 = files['file2_path']
        file2_byte_content = file2.read()

        data2 = json.loads(file2_byte_content)
        file2_data = json.dumps(data2, indent=4, sort_keys=True)

        file1 = logic.Filereader(file1_data)
        file1.unset_fields()
        file1.set_fields()
        file2 = logic.Filereader(file2_data)
        file2.unset_fields()
        file2.set_fields()

        dc = logic.DegreeComparision(file1.courses, file2.courses, 0.7)
        dc.unset_fields()
        dc.extract_description_of_courses()

        similarity_cal_res = dc.calculate_similarity()

        return similarity_cal_res, 200


API.add_resource(CompareECTS, '/compare/ects')
API.add_resource(CompareCourses, '/compare/similarity')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=5000)
