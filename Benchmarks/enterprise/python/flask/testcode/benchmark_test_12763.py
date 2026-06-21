# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def coalesce_blank(value):
    return value or ''

def BenchmarkTest12763():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
