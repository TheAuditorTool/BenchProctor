# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest41371(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
