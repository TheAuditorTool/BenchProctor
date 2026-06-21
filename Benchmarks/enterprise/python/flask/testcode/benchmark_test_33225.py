# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest33225():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
