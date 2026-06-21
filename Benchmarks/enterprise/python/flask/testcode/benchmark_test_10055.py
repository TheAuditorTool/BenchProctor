# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest10055(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
