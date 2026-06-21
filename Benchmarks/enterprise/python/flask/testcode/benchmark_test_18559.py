# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18559():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
