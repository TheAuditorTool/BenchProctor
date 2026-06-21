# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest81020(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
