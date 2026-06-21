# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def BenchmarkTest18527():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
