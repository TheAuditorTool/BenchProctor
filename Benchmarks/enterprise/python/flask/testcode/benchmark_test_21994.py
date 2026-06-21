# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest21994():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
