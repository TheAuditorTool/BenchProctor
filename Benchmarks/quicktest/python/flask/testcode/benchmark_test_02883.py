# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest02883():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
