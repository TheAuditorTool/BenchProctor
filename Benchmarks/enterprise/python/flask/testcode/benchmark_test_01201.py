# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest01201():
    multipart_value = request.form.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    eval(compile("with open('/var/uploads/' + str(data), 'wb') as fh:\n    fh.write(b'data')", '<sink>', 'exec'))
    return jsonify({"result": "success"})
