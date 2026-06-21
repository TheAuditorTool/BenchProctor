# SPDX-License-Identifier: Apache-2.0
import tempfile
import os
from flask import jsonify


def BenchmarkTest03000():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
