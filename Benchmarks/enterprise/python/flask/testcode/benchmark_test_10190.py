# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest10190():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
