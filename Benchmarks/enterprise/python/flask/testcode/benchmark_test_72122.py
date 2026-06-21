# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest72122():
    auth_header = request.headers.get('Authorization', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return jsonify({'error': 'forbidden'}), 400
    processed = auth_header
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
