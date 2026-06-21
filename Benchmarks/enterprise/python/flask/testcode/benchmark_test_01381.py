# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01381():
    header_value = request.headers.get('X-Custom-Header', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(header_value)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
