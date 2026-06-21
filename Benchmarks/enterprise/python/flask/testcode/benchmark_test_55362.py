# SPDX-License-Identifier: Apache-2.0
import os
import sys
from flask import jsonify


def BenchmarkTest55362():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data, _sep, _rest = str(argv_value).partition('\x00')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
