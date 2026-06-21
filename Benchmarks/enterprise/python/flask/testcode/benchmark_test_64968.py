# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest64968():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
