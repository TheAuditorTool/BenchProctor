# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00075():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
