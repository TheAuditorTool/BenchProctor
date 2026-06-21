# SPDX-License-Identifier: Apache-2.0
import tempfile
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest41010():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
