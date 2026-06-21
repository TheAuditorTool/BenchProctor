# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest02271():
    stdin_value = input('input: ')
    request_state['last_input'] = stdin_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
