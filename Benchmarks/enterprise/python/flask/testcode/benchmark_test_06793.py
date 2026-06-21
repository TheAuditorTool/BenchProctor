# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import request, jsonify


def BenchmarkTest06793():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
