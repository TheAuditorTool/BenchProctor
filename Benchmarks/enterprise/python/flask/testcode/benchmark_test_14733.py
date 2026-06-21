# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest14733():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
