# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest11807(path_param):
    path_value = path_param
    data = f'{path_value}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
