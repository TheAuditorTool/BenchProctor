# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest70712(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
