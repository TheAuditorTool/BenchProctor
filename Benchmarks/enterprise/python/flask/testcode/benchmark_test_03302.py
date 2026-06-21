# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest03302():
    stdin_value = input('input: ')
    def normalize(value):
        return value.strip()
    data = normalize(stdin_value)
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
