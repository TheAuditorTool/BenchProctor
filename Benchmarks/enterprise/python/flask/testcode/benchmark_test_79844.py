# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest79844():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return jsonify({"result": "success"})
