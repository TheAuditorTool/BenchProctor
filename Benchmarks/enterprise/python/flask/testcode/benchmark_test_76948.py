# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest76948(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
