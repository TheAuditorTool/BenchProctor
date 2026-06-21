# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73697():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
