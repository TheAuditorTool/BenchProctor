# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest33355():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
