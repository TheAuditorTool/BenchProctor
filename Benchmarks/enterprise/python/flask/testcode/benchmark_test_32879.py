# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest32879():
    cookie_value = request.cookies.get('session_token', '')
    os.remove(str(cookie_value))
    return jsonify({"result": "success"})
