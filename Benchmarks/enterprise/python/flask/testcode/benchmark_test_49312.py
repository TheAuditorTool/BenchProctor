# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest49312(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
