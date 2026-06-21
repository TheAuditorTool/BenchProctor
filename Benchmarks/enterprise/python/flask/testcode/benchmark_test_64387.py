# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest64387():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
