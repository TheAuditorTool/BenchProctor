# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10964():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
