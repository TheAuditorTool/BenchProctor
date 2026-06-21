# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import tempfile


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest07547():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
