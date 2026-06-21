# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest42926(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
