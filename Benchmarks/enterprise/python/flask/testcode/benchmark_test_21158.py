# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
from flask import jsonify


def BenchmarkTest21158():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = argv_value if argv_value else 'default'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
