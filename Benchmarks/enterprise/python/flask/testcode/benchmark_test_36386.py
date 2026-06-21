# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest36386():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
