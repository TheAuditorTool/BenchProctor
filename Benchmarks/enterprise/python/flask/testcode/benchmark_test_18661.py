# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest18661(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
