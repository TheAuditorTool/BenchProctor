# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest53614():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
