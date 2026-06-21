# SPDX-License-Identifier: Apache-2.0
import secrets
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest59968(path_param):
    path_value = path_param
    data = unquote(path_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
