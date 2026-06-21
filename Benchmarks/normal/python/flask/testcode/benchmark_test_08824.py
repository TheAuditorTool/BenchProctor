# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08824():
    multipart_value = request.form.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
