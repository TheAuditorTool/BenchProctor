# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest10889():
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    if time.time() > 1000000000:
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
