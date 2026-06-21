# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest52406():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
