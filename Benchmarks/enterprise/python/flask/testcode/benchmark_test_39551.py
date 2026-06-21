# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39551():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
