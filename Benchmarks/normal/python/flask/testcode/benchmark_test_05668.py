# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05668():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
