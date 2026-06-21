# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09229():
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return jsonify({"result": "success"})
