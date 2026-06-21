# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest65335(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
