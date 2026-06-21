# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27017():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
