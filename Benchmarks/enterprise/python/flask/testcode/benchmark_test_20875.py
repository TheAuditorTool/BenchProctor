# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest20875(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
