# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest66041(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
