# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest42497(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
