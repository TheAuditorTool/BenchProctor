# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


def BenchmarkTest10734(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
