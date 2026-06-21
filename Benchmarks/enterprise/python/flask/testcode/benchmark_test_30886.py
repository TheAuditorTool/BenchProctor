# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest30886():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    int(str(data))
    return jsonify({"result": "success"})
