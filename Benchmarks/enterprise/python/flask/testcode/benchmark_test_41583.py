# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def ensure_str(value):
    return str(value)

def BenchmarkTest41583():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
