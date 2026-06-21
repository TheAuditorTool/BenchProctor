# SPDX-License-Identifier: Apache-2.0
import subprocess
import sys
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest48734():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ns = SimpleNamespace(payload=argv_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
