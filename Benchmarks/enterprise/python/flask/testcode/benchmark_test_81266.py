# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81266():
    auth_header = request.headers.get('Authorization', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(auth_header)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
