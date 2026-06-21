# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest57297():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
