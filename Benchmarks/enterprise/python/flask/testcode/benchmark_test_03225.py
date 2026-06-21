# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest03225(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    session['data'] = str(data)
    return jsonify({"result": "success"})
