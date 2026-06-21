# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import jsonify
import os
from types import SimpleNamespace


def BenchmarkTest77138(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
