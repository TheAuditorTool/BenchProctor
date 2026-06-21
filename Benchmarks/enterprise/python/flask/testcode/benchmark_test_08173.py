# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest08173():
    stdin_value = input('input: ')
    data = coalesce_blank(stdin_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
