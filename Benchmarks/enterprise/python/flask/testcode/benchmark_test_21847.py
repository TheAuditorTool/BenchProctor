# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest21847():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
