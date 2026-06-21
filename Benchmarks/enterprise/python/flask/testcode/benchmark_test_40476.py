# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def BenchmarkTest40476(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
