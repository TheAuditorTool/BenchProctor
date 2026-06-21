# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest55714():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
