# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def BenchmarkTest16690(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
