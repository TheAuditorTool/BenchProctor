# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest80320():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
