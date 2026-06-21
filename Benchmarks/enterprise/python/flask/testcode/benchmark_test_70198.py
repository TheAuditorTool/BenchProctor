# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest70198():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
