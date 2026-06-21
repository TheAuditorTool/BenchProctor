# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest32719():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
