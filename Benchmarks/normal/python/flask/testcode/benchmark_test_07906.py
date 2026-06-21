# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest07906(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
