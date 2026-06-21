# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06789():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
