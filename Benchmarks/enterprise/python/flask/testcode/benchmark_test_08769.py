# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08769():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
