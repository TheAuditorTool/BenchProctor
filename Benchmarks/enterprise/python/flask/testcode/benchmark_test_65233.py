# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65233():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = coalesce_blank(json_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
