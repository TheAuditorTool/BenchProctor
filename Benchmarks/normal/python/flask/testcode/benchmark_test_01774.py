# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import json
from flask import request, jsonify


def BenchmarkTest01774():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
