# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest04789(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
