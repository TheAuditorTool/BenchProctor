# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest07133(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
