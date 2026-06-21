# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest42098():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
