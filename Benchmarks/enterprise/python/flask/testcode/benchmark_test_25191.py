# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest25191():
    stdin_value = input('input: ')
    data = ensure_str(stdin_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
