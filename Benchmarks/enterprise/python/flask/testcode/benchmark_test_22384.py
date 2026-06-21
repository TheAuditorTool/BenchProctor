# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest22384(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
