# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest16535():
    host_value = request.headers.get('Host', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
