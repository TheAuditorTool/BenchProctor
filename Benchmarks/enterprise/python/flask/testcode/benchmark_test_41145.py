# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import jsonify
import os


def BenchmarkTest41145(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
