# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest22767(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    os.remove(str(data))
    return jsonify({"result": "success"})
