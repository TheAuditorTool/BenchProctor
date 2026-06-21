# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15224():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
