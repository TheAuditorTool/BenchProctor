# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37018():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
