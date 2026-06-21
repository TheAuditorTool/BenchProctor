# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
import subprocess


def BenchmarkTest36221():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
