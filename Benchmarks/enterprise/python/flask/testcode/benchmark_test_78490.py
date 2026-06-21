# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest78490():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
