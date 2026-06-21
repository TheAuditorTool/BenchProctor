# SPDX-License-Identifier: Apache-2.0
import os
import shlex
import json
from flask import request, jsonify


def BenchmarkTest52214():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
