# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest24214(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
