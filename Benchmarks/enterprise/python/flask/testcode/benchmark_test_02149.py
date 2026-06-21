# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest02149():
    header_value = request.headers.get('X-Custom-Header', '')
    data = coalesce_blank(header_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
