# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest54766(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
