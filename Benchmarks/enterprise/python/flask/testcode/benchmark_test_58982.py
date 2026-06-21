# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest58982(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
