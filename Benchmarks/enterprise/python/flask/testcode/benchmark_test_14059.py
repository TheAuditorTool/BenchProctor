# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest14059():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    int(str(data))
    return jsonify({"result": "success"})
