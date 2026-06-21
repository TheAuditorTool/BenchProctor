# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18576():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
