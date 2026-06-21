# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09733():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
