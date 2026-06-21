# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


request_state: dict[str, str] = {}

def BenchmarkTest19588():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    json.loads(data)
    return jsonify({"result": "success"})
