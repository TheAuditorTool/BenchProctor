# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import subprocess


def BenchmarkTest12407():
    header_value = request.headers.get('X-Custom-Header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
