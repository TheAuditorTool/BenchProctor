# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest16772():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    processed = shlex.quote(forwarded_ip)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
