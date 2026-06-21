# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest37496():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = to_text(json_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
