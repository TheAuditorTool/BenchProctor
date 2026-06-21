# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest51119(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
