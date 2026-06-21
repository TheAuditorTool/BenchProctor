# SPDX-License-Identifier: Apache-2.0
from flask import session
import json
from flask import request, jsonify


def BenchmarkTest61617():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
