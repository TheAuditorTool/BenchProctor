# SPDX-License-Identifier: Apache-2.0
import os
import shlex
import sys
from flask import jsonify


def BenchmarkTest51351():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
