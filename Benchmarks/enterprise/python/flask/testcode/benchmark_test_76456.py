# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest76456(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
