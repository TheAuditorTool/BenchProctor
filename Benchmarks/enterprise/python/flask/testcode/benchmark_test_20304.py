# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20304():
    ua_value = request.headers.get('User-Agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    processed = data[:64]
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
