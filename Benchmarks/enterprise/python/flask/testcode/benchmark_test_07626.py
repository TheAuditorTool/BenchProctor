# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
from flask import jsonify


def BenchmarkTest07626():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = ' '.join(str(argv_value).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return jsonify({"result": "success"})
