# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest53524(path_param):
    path_value = path_param
    data = unquote(path_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
