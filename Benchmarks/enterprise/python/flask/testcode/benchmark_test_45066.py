# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest45066(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
