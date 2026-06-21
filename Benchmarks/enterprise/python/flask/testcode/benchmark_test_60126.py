# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest60126():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = ua_value
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
