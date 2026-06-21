# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest10198():
    stdin_value = input('input: ')
    if stdin_value:
        data = stdin_value
    else:
        data = ''
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
