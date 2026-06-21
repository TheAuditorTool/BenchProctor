# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time


def normalise_input(value):
    return value.strip()

def BenchmarkTest15336():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
