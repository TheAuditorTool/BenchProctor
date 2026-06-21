# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest32009(path_param):
    path_value = path_param
    return jsonify({'error': str(path_value), 'stack': repr(locals())}), 500
