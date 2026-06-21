# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest36210():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = normalise_input(json_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
