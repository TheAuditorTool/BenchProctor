# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import subprocess


def BenchmarkTest42066():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
