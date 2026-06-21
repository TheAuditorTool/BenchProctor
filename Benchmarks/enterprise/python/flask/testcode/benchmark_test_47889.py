# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47889():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
