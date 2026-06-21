# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest11595():
    stdin_value = input('input: ')
    data = stdin_value if stdin_value else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
