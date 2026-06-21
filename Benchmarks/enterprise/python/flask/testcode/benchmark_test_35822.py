# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35822():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
