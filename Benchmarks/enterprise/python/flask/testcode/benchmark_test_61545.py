# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61545():
    raw_body = request.get_data(as_text=True)
    try:
        result = int(str(raw_body))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
