# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest76984():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
