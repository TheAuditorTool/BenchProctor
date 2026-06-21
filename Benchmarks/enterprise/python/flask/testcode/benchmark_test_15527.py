# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15527():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
