# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import json


def BenchmarkTest08992():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
