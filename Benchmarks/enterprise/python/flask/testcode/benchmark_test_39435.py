# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest39435():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    os.remove(str(data))
    return jsonify({"result": "success"})
