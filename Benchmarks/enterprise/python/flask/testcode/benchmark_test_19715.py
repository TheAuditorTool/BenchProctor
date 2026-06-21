# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest19715(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
