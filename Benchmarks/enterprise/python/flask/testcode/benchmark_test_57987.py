# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest57987(path_param):
    path_value = path_param
    data = unquote(path_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
