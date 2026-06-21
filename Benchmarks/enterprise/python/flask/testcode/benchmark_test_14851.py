# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest14851():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
