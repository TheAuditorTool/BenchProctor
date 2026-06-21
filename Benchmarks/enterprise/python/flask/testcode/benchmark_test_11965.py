# SPDX-License-Identifier: Apache-2.0
import tempfile
from urllib.parse import unquote
from flask import jsonify
import os


def BenchmarkTest11965(path_param):
    path_value = path_param
    data = unquote(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
