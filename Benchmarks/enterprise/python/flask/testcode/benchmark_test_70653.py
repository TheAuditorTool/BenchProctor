# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest70653():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})
