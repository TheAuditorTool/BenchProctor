# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import runpy


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest39305():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})
