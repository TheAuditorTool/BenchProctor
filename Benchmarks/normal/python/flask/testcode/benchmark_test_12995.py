# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest12995():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})
