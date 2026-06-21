# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
from flask import jsonify


def BenchmarkTest15976():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    subprocess.Popen('echo ' + str(argv_value), shell=True).wait()
    return jsonify({"result": "success"})
