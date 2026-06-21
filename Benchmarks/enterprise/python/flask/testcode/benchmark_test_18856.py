# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18856():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
