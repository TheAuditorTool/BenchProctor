# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest08536(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
