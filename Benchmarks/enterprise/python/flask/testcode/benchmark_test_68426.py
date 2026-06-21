# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest68426():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    session['data'] = str(json_value)
    return jsonify({"result": "success"})
