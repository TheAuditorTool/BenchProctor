# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23532():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
