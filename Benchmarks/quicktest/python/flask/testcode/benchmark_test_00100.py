# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest00100():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    os.seteuid(65534)
    return jsonify({"result": "success"})
