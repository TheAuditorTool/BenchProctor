# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest54738():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
