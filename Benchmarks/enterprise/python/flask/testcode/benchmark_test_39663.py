# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest39663(path_param):
    path_value = path_param
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(path_value)}
