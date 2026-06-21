# SPDX-License-Identifier: Apache-2.0
import os
import base64
from flask import request, jsonify


def BenchmarkTest59044():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
