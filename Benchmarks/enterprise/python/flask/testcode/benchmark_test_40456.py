# SPDX-License-Identifier: Apache-2.0
from flask import session
import json
from flask import request, jsonify


def BenchmarkTest40456():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    session['user'] = str(data)
    return jsonify({"result": "success"})
