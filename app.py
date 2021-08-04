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

        args = request.args
        path1 = args['file1_path']
        path2 = args['file2_path']

        file1 = logic.Filereader(path1)
        file1.set_fields()

        file2 = logic.Filereader(path2)
        file2.set_fields()

        dc = logic.DegreeComparision(file1.courses, file2.courses, 0.5)
        dc.extract_description_of_courses()

        ects_compare_res = dc.compare_ects(file1.ects, file2.ects)

        out = json.dumps(ects_compare_res)
        return out, 200


class CompareCourses(Resource):

    @staticmethod
    def get():
        args = request.args
        print(args)  # For debugging
        path1 = args['file1_path']
        path2 = args['file2_path']

        file1 = logic.Filereader(path1)
        file1.set_fields()
        file2 = logic.Filereader(path2)
        file2.set_fields()

        dc = logic.DegreeComparision(file1.courses, file2.courses, 0.7)
        dc.extract_description_of_courses()

        similarity_cal_res = dc.calculate_similarity()

        return similarity_cal_res, 200

API.add_resource(CompareECTS, '/compare/ects')
API.add_resource(CompareCourses, '/compare/similarity')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')