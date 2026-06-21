# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest74472():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
