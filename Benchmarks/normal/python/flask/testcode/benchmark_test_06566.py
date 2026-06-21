# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def to_text(value):
    return str(value).strip()

def BenchmarkTest06566():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
