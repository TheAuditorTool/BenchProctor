# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest40022():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
