# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest11920():
    origin_value = request.headers.get('Origin', '')
    processed = shlex.quote(origin_value)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
