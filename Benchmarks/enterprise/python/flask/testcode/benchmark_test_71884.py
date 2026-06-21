# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest71884(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    eval(compile("_resp = requests.get(str(data))\ndb.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
