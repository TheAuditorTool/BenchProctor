# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08386():
    xml_value = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
