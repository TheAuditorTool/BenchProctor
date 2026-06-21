# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest50278():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
