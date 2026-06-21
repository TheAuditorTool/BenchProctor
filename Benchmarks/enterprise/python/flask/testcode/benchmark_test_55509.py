# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55509():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
