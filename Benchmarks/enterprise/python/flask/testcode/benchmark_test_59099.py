# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def BenchmarkTest59099(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
