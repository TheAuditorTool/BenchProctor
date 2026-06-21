# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import jsonify


def BenchmarkTest02011(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
