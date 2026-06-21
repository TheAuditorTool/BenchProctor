# SPDX-License-Identifier: Apache-2.0
import os
import sys
from flask import jsonify


def BenchmarkTest36916():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    def normalize(value):
        return value.strip()
    data = normalize(argv_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
