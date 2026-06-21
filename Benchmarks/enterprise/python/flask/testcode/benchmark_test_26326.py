# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def BenchmarkTest26326(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
