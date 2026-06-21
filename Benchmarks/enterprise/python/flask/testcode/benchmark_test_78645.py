# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78645():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
