# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest72384(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
