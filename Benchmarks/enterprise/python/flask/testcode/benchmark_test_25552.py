# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest25552():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
