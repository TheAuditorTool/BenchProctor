# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest18580():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
