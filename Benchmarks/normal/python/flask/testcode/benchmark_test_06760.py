# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06760():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
