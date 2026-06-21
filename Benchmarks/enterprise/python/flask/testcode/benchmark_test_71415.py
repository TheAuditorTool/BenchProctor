# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def BenchmarkTest71415(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
