# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest43224(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
