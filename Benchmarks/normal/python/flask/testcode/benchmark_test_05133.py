# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest05133():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
