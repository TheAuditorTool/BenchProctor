# SPDX-License-Identifier: Apache-2.0
import os
import sys
from flask import jsonify


def BenchmarkTest55516():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = (lambda v: v.strip())(argv_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
