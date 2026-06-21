# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest13711():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
