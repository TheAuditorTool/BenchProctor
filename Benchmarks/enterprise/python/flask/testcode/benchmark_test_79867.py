# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest79867():
    multipart_value = request.form.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    processed = data[:64]
    session['data'] = str(processed)
    return jsonify({"result": "success"})
