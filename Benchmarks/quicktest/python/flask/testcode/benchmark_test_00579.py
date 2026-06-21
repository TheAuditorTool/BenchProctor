# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest00579(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
