# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest62690(path_param):
    path_value = path_param
    data = to_text(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
