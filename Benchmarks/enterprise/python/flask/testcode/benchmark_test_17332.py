# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
from types import SimpleNamespace
import subprocess


def BenchmarkTest17332():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
