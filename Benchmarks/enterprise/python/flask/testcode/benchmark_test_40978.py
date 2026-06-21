# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest40978(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
