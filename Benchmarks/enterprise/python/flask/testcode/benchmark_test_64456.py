# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64456():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    reader = make_reader(argv_value)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
