# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest30791():
    stdin_value = input('input: ')
    data, _sep, _rest = str(stdin_value).partition('\x00')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
