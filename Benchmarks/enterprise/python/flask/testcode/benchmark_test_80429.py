# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest80429(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
