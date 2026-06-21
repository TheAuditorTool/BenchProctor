# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def BenchmarkTest45953():
    user_id = request.args.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
