# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53390():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
