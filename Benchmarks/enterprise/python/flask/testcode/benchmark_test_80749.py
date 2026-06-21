# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest80749():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
