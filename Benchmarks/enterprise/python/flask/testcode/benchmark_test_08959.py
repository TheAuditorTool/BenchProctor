# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


def BenchmarkTest08959(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
