# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest51849():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
