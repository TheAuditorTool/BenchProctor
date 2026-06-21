# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest73467(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
