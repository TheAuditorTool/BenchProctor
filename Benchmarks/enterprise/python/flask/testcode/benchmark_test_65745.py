# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
from flask import jsonify


def BenchmarkTest65745():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
