# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest07852():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
