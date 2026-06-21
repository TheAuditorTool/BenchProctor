# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import jsonify
import os


def BenchmarkTest26821(path_param):
    path_value = path_param
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(path_value))
    return jsonify({"result": "success"})
