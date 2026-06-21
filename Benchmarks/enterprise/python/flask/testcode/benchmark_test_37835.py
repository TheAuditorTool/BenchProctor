# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest37835(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
