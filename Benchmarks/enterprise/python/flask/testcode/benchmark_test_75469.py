# SPDX-License-Identifier: Apache-2.0
import os
import shlex
import base64
from flask import request, jsonify


def BenchmarkTest75469():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
