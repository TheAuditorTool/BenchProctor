# SPDX-License-Identifier: Apache-2.0
import os
import base64
from flask import request, jsonify


def BenchmarkTest06826():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
