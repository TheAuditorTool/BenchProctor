# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22986():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
