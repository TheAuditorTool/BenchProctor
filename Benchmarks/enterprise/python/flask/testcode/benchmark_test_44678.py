# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import json


def BenchmarkTest44678():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
