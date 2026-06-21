# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78862():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
