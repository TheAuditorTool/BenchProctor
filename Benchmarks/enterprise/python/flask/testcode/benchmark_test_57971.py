# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest57971():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = str(ast.literal_eval(profile_value))
    except (ValueError, SyntaxError):
        data = profile_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
