# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest58529(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
