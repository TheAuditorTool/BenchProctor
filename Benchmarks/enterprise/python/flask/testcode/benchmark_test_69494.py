# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest69494():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
