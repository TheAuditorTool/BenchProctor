# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest65338():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
