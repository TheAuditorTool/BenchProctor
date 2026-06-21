# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest71486(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
