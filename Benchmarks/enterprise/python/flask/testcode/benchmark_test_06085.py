# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06085():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = coalesce_blank(json_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
