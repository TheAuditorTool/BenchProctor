# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest77156(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
