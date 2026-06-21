# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest45420():
    stdin_value = input('input: ')
    parts = []
    for token in str(stdin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
