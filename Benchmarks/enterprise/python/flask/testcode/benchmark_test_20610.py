# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest20610(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    eval(compile("subprocess.Popen('echo ' + str(data), shell=True).wait()", '<sink>', 'exec'))
    return jsonify({"result": "success"})
