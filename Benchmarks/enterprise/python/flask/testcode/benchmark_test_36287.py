# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest36287():
    stdin_value = input('input: ')
    data, _sep, _rest = str(stdin_value).partition('\x00')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
