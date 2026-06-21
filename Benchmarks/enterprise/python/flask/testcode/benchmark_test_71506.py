# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time


def relay_value(value):
    return value

def BenchmarkTest71506():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
