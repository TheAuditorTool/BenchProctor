# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45948():
    user_id = request.args.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
