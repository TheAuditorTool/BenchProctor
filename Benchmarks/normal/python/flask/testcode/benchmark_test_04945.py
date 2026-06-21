# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest04945(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
