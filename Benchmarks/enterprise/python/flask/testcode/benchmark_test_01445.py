# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest01445(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
