# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest05680():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
