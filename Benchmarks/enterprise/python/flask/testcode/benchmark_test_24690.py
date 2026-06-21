# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time


def BenchmarkTest24690():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})
