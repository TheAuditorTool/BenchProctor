# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def relay_value(value):
    return value

def BenchmarkTest08752():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
