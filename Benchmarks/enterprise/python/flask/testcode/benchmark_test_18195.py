# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest18195():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
