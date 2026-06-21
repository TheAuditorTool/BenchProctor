# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import json


def BenchmarkTest12514(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
