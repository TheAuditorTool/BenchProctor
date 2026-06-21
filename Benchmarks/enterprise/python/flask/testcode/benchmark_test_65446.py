# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest65446(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
