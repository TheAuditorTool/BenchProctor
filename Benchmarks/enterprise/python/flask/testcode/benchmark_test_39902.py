# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest39902():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
