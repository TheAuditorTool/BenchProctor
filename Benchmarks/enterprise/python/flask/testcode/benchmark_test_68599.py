# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def BenchmarkTest68599(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
