# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42840():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
