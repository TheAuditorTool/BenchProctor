# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest09343():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
