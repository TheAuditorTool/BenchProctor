# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest77132():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return jsonify({"result": "success"})
