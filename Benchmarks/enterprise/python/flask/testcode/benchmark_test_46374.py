# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest46374():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
