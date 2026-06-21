# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest54895(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
