# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest10023():
    header_value = request.headers.get('X-Custom-Header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = data[:64]
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
