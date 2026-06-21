# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def BenchmarkTest20683():
    stdin_value = input('input: ')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(stdin_value)
    data = collected
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
