# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60355():
    user_id = request.args.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
