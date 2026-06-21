# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest54805():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return jsonify({"result": "success"})
