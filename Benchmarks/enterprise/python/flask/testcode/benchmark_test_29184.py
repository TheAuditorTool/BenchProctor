# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json


def BenchmarkTest29184(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
