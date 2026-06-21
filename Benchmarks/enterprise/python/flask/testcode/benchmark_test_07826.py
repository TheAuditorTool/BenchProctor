# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07826():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
