# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import socket


def BenchmarkTest06780():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
