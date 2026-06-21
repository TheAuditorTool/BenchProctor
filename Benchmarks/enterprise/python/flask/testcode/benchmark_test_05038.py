# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest05038(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
