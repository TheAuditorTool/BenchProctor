# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest50808():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
