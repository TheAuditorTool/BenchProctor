# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest01488():
    stdin_value = input('input: ')
    def normalize(value):
        return value.strip()
    data = normalize(stdin_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
