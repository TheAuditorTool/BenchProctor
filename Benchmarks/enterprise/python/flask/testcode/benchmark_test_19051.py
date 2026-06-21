# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19051():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
