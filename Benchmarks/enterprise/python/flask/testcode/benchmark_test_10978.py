# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest10978(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
