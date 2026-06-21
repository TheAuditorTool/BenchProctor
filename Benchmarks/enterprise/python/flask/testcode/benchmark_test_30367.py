# SPDX-License-Identifier: Apache-2.0
import os
import shlex
import sys
from flask import jsonify


def BenchmarkTest30367():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data, _sep, _rest = str(argv_value).partition('\x00')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
