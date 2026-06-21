# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time


def normalise_input(value):
    return value.strip()

def BenchmarkTest08382():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    if time.time() > 1000000000:
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
