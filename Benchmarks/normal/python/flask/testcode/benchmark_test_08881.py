# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest08881():
    origin_value = request.headers.get('Origin', '')
    data = coalesce_blank(origin_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
