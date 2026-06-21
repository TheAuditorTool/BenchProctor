# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02664():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
