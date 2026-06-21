# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest33984():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
