# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest50303():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
