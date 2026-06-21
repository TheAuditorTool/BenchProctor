# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest35398():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
