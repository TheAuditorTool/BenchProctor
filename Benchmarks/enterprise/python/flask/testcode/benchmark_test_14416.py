# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import json


def BenchmarkTest14416(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
