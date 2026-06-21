# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest26787():
    auth_header = request.headers.get('Authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
