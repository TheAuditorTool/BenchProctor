# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74164():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
