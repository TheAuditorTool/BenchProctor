# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest41229():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
