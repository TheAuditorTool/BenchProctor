# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest09296():
    stdin_value = input('input: ')
    data = to_text(stdin_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
