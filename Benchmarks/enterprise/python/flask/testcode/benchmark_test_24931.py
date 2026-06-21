# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24931():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(json_value)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
