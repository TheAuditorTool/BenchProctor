# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest63449():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    eval(compile("with open('/var/log/app_audit.log', 'a') as fh:\n    fh.write(str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
