# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


request_state: dict[str, str] = {}

def BenchmarkTest72855():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
