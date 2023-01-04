from flask import jsonify, abort
from flask_restful import Resource
import json


class provaResource(Resource):
    def get(self):
        f = open('pycertify/provas/ia-900/en-us/prova_ia_900_en.json')
        prova = json.load(f)
        return jsonify(prova)