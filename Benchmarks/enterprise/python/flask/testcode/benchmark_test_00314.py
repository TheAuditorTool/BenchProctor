# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00314():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
