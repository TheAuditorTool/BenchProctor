# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11219():
    auth_header = request.headers.get('Authorization', '')
    if auth_header not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = auth_header
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
