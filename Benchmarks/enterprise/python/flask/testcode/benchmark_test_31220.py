# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest31220():
    origin_value = request.headers.get('Origin', '')
    data = to_text(origin_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
