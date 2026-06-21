# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import time


def relay_value(value):
    return value

def BenchmarkTest07390():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
