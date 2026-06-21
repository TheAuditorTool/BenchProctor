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

def BenchmarkTest33012():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    if time.time() > 1000000000:
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
