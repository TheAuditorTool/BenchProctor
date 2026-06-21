# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time


request_state: dict[str, str] = {}

def BenchmarkTest28573():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
