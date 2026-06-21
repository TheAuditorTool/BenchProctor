# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest49610():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    int(str(data))
    return jsonify({"result": "success"})
