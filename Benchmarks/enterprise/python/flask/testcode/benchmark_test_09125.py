# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest09125(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
