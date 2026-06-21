# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest74613():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
