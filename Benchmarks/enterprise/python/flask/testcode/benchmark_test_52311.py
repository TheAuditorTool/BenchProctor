# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest52311():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    if time.time() > 1000000000:
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
