# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest69989(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
