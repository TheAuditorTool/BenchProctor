# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import time


def BenchmarkTest72759(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    if time.time() > 1000000000:
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
