# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest70556():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
