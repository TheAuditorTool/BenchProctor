# SPDX-License-Identifier: Apache-2.0
import subprocess
import json
from flask import request, jsonify


def BenchmarkTest45192():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
