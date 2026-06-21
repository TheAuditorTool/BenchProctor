# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify


def BenchmarkTest01412():
    stdin_value = input('input: ')
    data = ' '.join(str(stdin_value).split())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
