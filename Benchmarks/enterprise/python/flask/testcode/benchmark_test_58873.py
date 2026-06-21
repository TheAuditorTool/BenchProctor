# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest58873():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
