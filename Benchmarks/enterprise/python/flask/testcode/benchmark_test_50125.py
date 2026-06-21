# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest50125():
    stdin_value = input('input: ')
    if stdin_value:
        data = stdin_value
    else:
        data = ''
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
