# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def normalise_input(value):
    return value.strip()

def BenchmarkTest58398():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    eval(compile('s = socket.create_connection((str(data), 80))\ns.close()', '<sink>', 'exec'))
    return jsonify({"result": "success"})
