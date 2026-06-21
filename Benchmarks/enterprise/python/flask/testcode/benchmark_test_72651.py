# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
import subprocess


def BenchmarkTest72651():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
