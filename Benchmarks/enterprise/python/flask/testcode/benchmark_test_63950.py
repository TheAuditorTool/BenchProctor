# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest63950():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
