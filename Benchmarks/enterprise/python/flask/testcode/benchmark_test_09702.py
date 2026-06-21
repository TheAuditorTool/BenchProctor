# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import time


def normalise_input(value):
    return value.strip()

def BenchmarkTest09702():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
