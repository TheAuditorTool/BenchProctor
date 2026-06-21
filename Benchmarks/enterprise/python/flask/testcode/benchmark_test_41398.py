# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest41398(path_param):
    path_value = path_param
    data = relay_value(path_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
