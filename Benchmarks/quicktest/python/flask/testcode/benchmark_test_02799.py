# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest02799():
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
