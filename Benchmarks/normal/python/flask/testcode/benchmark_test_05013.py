# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import json


def BenchmarkTest05013(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
