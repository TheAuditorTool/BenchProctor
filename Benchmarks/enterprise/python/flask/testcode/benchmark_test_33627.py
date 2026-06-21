# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def BenchmarkTest33627(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
