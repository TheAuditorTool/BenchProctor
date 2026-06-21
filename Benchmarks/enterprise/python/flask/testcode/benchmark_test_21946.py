# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest21946(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
