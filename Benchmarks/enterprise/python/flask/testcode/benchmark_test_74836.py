# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import json


def BenchmarkTest74836():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
