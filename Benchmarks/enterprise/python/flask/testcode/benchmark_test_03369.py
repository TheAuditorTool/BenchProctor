# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest03369():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
