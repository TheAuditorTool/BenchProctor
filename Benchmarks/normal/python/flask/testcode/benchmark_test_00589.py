# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest00589(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
