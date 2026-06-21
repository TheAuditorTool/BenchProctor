# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest15717():
    stdin_value = input('input: ')
    def normalize(value):
        return value.strip()
    data = normalize(stdin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return jsonify({"result": "success"})
