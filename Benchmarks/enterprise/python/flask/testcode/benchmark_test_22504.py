# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def relay_value(value):
    return value

def BenchmarkTest22504():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
