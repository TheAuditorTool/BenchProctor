# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest31098(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
