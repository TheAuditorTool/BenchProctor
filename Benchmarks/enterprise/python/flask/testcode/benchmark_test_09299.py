# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest09299():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
