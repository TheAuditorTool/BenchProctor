# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest04544():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
