# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest24722():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
