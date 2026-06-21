# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import request, jsonify


def BenchmarkTest69244():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
