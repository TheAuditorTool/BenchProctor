# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest13906():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
