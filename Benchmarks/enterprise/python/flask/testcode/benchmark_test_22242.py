# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22242():
    referer_value = request.headers.get('Referer', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(referer_value)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
