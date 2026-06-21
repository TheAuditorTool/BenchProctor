# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import jsonify
from types import SimpleNamespace
import subprocess


def BenchmarkTest16590(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
